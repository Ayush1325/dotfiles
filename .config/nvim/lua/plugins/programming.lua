local function on_attach(client, bufnr)
	local function buf_set_option(...) vim.api.nvim_buf_set_option(bufnr, ...) end
	buf_set_option('omnifunc', 'v:lua.vim.lsp.omnifunc')
end

local function default_lsp_config()
	local capabilities = require("cmp_nvim_lsp").default_capabilities()
	return {
		capabilities = capabilities,
		on_attach = on_attach,
	}
end

return {
	{
		"neovim/nvim-lspconfig",
		dependencies = {
			"tamago324/nlsp-settings.nvim",
		},
		config = function()
			require("lspconfig").cmake.setup(default_lsp_config())
			require("lspconfig").sqlls.setup(default_lsp_config())
			require("lspconfig").pyright.setup(default_lsp_config())
			require("lspconfig").gopls.setup(default_lsp_config())
		end
	},
	{
		"tamago324/nlsp-settings.nvim",
		config = function()
			local nlspsettings = require("nlspsettings")
			nlspsettings.setup({
				config_home = vim.fn.stdpath('config') .. '/nlsp-settings',
				local_settings_dir = ".nlsp-settings",
				local_settings_root_markers_fallback = { '.git' },
				append_default_schemas = true,
				loader = 'json'
			})
		end
	},
	{
		"lewis6991/gitsigns.nvim",
		config = true
	},
	{
		"simrat39/rust-tools.nvim",
		dependencies = {
			"neovim/nvim-lspconfig",
			"tamago324/nlsp-settings.nvim",
		},
		config = function()
			require("rust-tools").setup(default_lsp_config())
		end
	},
	{
		"folke/neodev.nvim",
		dependencies = {
			"neovim/nvim-lspconfig",
			"tamago324/nlsp-settings.nvim",
		},
		config = function()
			require("neodev").setup({})
			require('lspconfig').lua_ls.setup(default_lsp_config())
		end
	},
	{
		"p00f/clangd_extensions.nvim",
		dependencies = {
			"neovim/nvim-lspconfig",
			"tamago324/nlsp-settings.nvim",
		},
		config = function()
			require('lspconfig').clangd.setup(default_lsp_config())
		end
	},
	{
		"nvim-treesitter/nvim-treesitter-context",
		config = function ()
			require('treesitter-context').setup({})
		end
	},
	{
		"zbirenbaum/copilot.lua",
		event = "InsertEnter",
		opts = {
			suggestion = {
				auto_trigger = true,
				keymap = {
					accept = "<M-CR>",
				}
			}
		},
		config = true
	},
	{
		'akinsho/flutter-tools.nvim',
		lazy = false,
		dependencies = {
			'nvim-lua/plenary.nvim',
			'stevearc/dressing.nvim', -- optional for vim.ui.select
		},
		config = true,
	},
}
