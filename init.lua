vim.g.mapleader = " " -- Set the space key as the leader key for custom keybindings

require("kmill.settings")
require("kmill.lazy")
require("kmill.maps")

-- Clipboard
vim.api.nvim_set_option("clipboard", "unnamedplus")
