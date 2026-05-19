require('vim._core.ui2').enable({})
vim.loader.enable() -- Lua bytecode cache for faster startup

-- Setup leader
vim.g.mapleader = " "
vim.g.maplocalleader = "\\"

vim.g.termguicolors = true

vim.o.nu = true
vim.o.relativenumber = true
vim.o.cursorline = true
vim.o.expandtab = true
vim.o.hlsearch = true
vim.o.incsearch = true
vim.o.wrap = false
-- Clipboard
vim.schedule(function()
  vim.o.clipboard = 'unnamedplus'
end) -- deferred to avoid startup slowdown

-- Better Undo
vim.opt.undofile = true
vim.cmd.packadd("nvim.undotree")

vim.keymap.set('n', "grn", vim.lsp.buf.rename, { desc = "Rename" })
vim.keymap.set('n', "gra", vim.lsp.buf.code_action, { desc = "Code Action" })
vim.keymap.set('n', 'grf', vim.diagnostic.open_float, { desc = 'Line Diagnostics' })
vim.keymap.set('n', "<leader>bf", vim.lsp.buf.format, { desc = "Format buffer" })
vim.keymap.set('n', "<leader>bd", "<cmd>bd<CR>", { desc = "Close buffer" })
vim.keymap.set('n', "<leader>bn", "<cmd>echo expand('%:p')<CR>", { desc = "Display File Name" })

-- Theme
require('theme')
vim.pack.add({
        'https://github.com/lukas-reineke/indent-blankline.nvim',
        'https://github.com/nvim-tree/nvim-web-devicons',
        'https://github.com/nvim-lualine/lualine.nvim'
})
require('ibl').setup({
    scope = {
        enabled = true,
        show_start = true,
        show_end = false,
    },
})
require('lualine').setup({})

-- Which Key
vim.pack.add({'https://github.com/folke/which-key.nvim'})
require('which-key').setup()
vim.keymap.set('n', '<leader>?', function()
    require('which-key').show({ global = false })
end, { desc = 'Buffer Local Keymaps (which-key)' })

-- Parens
vim.pack.add({
        'https://github.com/windwp/nvim-autopairs',
        'https://github.com/HiPhish/rainbow-delimiters.nvim'
})
require('nvim-autopairs').setup()
require('rainbow-delimiters.setup').setup({})

-- Auto Save
vim.o.autowriteall = true

-- Git
vim.pack.add({
        'https://github.com/NeogitOrg/neogit',
        'https://github.com/lewis6991/gitsigns.nvim',
        'https://github.com/sindrets/diffview.nvim'
})
require('neogit').setup({})
vim.keymap.set('n', '<leader>gg', require('neogit').open, { desc = 'Open Neogit' })
require('gitsigns').setup()

-- Telescope
vim.pack.add({
        'https://github.com/nvim-telescope/telescope.nvim',
        'https://github.com/nvim-lua/plenary.nvim'
})
require('telescope').setup({})

vim.keymap.set('n', '<leader>ff', require('telescope.builtin').find_files, { desc = 'Telescope find files' })
vim.keymap.set('n', '<leader>fg', require('telescope.builtin').live_grep, { desc = 'Telescope live grep' })
vim.keymap.set('n', '<leader>fb', require('telescope.builtin').buffers, { desc = 'Telescope buffers' })
vim.keymap.set('n', '<leader>fh', require('telescope.builtin').help_tags, { desc = 'Telescope help tags' })

vim.keymap.set('n', 'gd', require('telescope.builtin').lsp_definitions, { desc = 'List definitions' })
vim.keymap.set('n', 'grr', require('telescope.builtin').lsp_references, { desc = 'List LSP references' })
vim.keymap.set('n', 'grd', require('telescope.builtin').diagnostics, { desc = 'Diagnostics' })

-- Completion
vim.pack.add({
        'https://github.com/saghen/blink.lib',
        'https://github.com/saghen/blink.cmp'
})
local cmp = require('blink.cmp')
cmp.build():wait(60000)
cmp.setup({
    keymap = { preset = 'super-tab' },
    signature = { enabled = true },
    sources = {
        default = { 'lsp', 'path', 'snippets', 'buffer' },
    },
})

-- LSP
vim.pack.add({
        'https://github.com/neovim/nvim-lspconfig',
        'https://github.com/j-hui/fidget.nvim',
        'https://github.com/folke/lazydev.nvim',
        'https://github.com/williamboman/mason.nvim'
})

require('fidget').setup({})
require('mason').setup()
require('lazydev').setup({
    library = {
        {
            path = '${3rd}/luv/library',
            words = { 'vim%.uv' },
        },
    },
})

local servers = {
    lua_ls = {},
    rust_analyzer = {},
    clangd = {},
    jsonls = {},
    pyright = {},
    gopls = {},
    emmet_language_server = {
        filetypes = { 'css', 'html', 'handlebars' },
    },
    html = {
        filetypes = { 'html', 'handlebars' },
    },
    bashls = {},
    tinymist = {},
}

for server, config in pairs(servers) do
    vim.lsp.config(server, config)
    vim.lsp.enable(server)
end

-- Treesitter
vim.pack.add({
        'https://github.com/romus204/tree-sitter-manager.nvim',
        'https://github.com/nvim-treesitter/nvim-treesitter-context'
})
require("tree-sitter-manager").setup({
        ensure_installed = {
                'bash', 'c', 'cpp', 'cmake', 'dockerfile', 'html', 'javascript',
                'json', 'kconfig', 'make', 'markdown', 'python', 'rst', 'rust',
                'sway', 'udev', 'zsh'
        },
})
require('treesitter-context').setup({})
