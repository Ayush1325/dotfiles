vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.cursorline = true
-- Clipboard
vim.opt.clipboard = "unnamedplus"
-- Persistant Undo
vim.opt.undofile = true

vim.keymap.set('n', "grn", vim.lsp.buf.rename, { desc = "Rename" })
vim.keymap.set('n', "gra", vim.lsp.buf.code_action, { desc = "Code Action" })
vim.keymap.set('n', "<leader>bf", vim.lsp.buf.format, { desc = "Format buffer" })
vim.keymap.set('n', "<leader>bd", "<cmd>bd<CR>", { desc = "Close buffer" })
vim.keymap.set('n', "<leader>bn", "<cmd>echo expand('%:p')<CR>", { desc = "Display File Name" })

return {
	{
		"hoob3rt/lualine.nvim",
		dependencies = { "kyazdani42/nvim-web-devicons", opt = true },
		config = true,
	},
	{
		"lukas-reineke/indent-blankline.nvim",
		main = "ibl",
		opts = {
			scope = {
				enabled = true,
				show_start = true,
				show_end = false,
			}
		},
		config = true
	},
	{
		"Pocco81/auto-save.nvim",
		config = true,
	},
	{
		"nvim-treesitter/nvim-treesitter",
		build = ":TSUpdate",
		opts = {
			ensure_installed = "all",
		},
	},
	{
		"nvim-treesitter/nvim-treesitter-context",
		dependencies = {
			"nvim-treesitter/nvim-treesitter"
		},
		config = function()
			require('treesitter-context').setup({})
		end
	},
	{
		"windwp/nvim-autopairs",
		config = true,
	},
	{
		"NeogitOrg/neogit",
		dependencies = {
			"nvim-lua/plenary.nvim", -- required
			"sindrets/diffview.nvim", -- optional - Diff integration
		},
		config = function()
			require('neogit').setup({})
			vim.keymap.set('n', "<leader>gg", require('neogit').open, { desc = "Open Neogit" })
		end
	},
	{
		'saghen/blink.cmp',
		dependencies = 'rafamadriz/friendly-snippets',
		version = '*',
		opts = {
			keymap = { preset = 'super-tab' },
			signature = { enabled = true },
			sources = {
				default = { 'lsp', 'path', 'snippets', 'buffer' },
			},
		},
		opts_extend = { "sources.default" }
	},
	{
		'neovim/nvim-lspconfig',
		dependencies = {
			'saghen/blink.cmp',
			'folke/neoconf.nvim'
		},
		opts = {
			servers = {
				lua_ls = {},
				rust_analyzer = {},
				clangd = {},
				jsonls = {},
				pyright = {},
				gopls = {},
				emmet_ls = {},
				tailwindcss = {},
                        	tinymist = {}
			}
		},
		config = function(_, opts)
			for server, config in pairs(opts.servers) do
				vim.lsp.config(server, config)
				vim.lsp.enable(server)
			end
		end
	},
	{
		'folke/neoconf.nvim',
		config = true,
	},
	{
		"williamboman/mason.nvim",
		config = true
	},
	{
		"folke/lazydev.nvim",
		ft = "lua", -- only load on lua files
		opts = {
			library = {
				-- See the configuration section for more details
				-- Load luvit types when the `vim.uv` word is found
				{ path = "${3rd}/luv/library", words = { "vim%.uv" } },
			},
		},
	},
	{
		"folke/which-key.nvim",
		event = "VeryLazy",
		opts = {},
		keys = {
			{
				"<leader>?",
				function()
					require("which-key").show({ global = false })
				end,
				desc = "Buffer Local Keymaps (which-key)",
			},
		},
	},
	{
		"lewis6991/gitsigns.nvim",
		config = true
	},
	{
		'nvim-telescope/telescope.nvim',
		tag = 'v0.2.0',
		dependencies = {
			'nvim-lua/plenary.nvim',
			{ "nvim-tree/nvim-web-devicons", opts = {} },
			{
				'nvim-telescope/telescope-fzf-native.nvim',
				build =
				'cmake -S. -Bbuild -DCMAKE_BUILD_TYPE=Release && cmake --build build --config Release'
			}
		},
		config = function()
			require('telescope').setup({})
			require('telescope').load_extension('fzf')

			local builtin = require('telescope.builtin')
			vim.keymap.set('n', '<leader>ff', builtin.find_files, { desc = 'Telescope find files' })
			vim.keymap.set('n', '<leader>fg', builtin.live_grep, { desc = 'Telescope live grep' })
			vim.keymap.set('n', '<leader>fb', builtin.buffers, { desc = 'Telescope buffers' })
			vim.keymap.set('n', '<leader>fh', builtin.help_tags, { desc = 'Telescope help tags' })

			vim.keymap.set('n', "gd", builtin.lsp_definitions, { desc = "List definations" })
			vim.keymap.set('n', "grr", builtin.lsp_references, { desc = "List LSP references" })
			vim.keymap.set('n', 'grd', builtin.diagnostics, { desc = "Diagnostics" })
		end
	},
	{
		"HiPhish/rainbow-delimiters.nvim",
		config = function()
			require('rainbow-delimiters.setup').setup({})
		end
	}
}
