vim.g.mapleader = " "

return {
	{
		"folke/which-key.nvim",
		dependencies = {
			"phaazon/hop.nvim",
			"nvim-telescope/telescope.nvim",
		},
		config = function()
			local telescope_builtin = require("telescope.builtin")

			local wk = require("which-key")
			wk.setup({})
			wk.register({
				b = {
					name = "Buffers",
					b = { telescope_builtin.buffers, "List Buffers" },
					c = { "<cmd>bd<CR>", "Close Buffer" },
					n = { "<cmd>echo expand('%:p')<CR>", "Display File Name" },
					f = { vim.lsp.buf.format, "Format Buffer" },
				},

				f = {
					name = "Files",
					f = { telescope_builtin.find_files, "Find Files in Workind dir" },
					g = { telescope_builtin.git_files, "Find Files Git" },
					l = { telescope_builtin.live_grep, "Live Grep" },
					s = { telescope_builtin.grep_string, "Grep String" },
				},

				g = {
					name = "Git",
					c = { telescope_builtin.git_commits, "List Git commits" },
					b = { telescope_builtin.git_bcommits, "List Buffere's commits" },
					t = { require('neogit').open, "Neogit" }
				},

				h = {
					name = "Help",
					t = { telescope_builtin.help_tags, "Help Tags" },
				},

				l = {
					name = "LSP",
					i = { telescope_builtin.lsp_implementations, "LSP Implementations" },
					d = { telescope_builtin.lsp_definitions, "LSP Definations" },
					c = { vim.lsp.buf.code_action, "Code Action" },
					r = { vim.lsp.buf.rename, "LSP Rename" },
					l = {
						name = "List",
						r = { telescope_builtin.lsp_references, "LSP References" },
						s = { telescope_builtin.lsp_document_symbols, "LSP Document Symbols" },
						w = { telescope_builtin.lsp_workspace_symbols, "LSP Workspace Symbols" },
					},
				},

				m = {
					name = "Motion",
					w = { require("hop").hint_words, "Hit Words" },
					l = { require("hop").hint_lines_skip_whitespace, "Hint Lines" },
					c = { require("hop").hint_char1, "Hint Char" },
					C = { require("hop").hint_char2, "Hint Char" },
				},
			}, { prefix = "<leader>" })
		end,
	},
}
