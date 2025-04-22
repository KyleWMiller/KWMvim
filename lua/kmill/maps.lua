vim.g.mapleader = " "
-- Define a helper function for creating keymaps with silent option enabled
local function map(mode, lhs, rhs)
	vim.keymap.set(mode, lhs, rhs, { silent = true })
end

map("n", "<leader>l", "<CMD>Lazy<CR>") -- Save the current buffer (file)

map("n", "<leader>mp", "<CMD>MarkdownPreviewToggle<CR>") -- Save the current buffer (file)

map("n", "<leader>w", "<CMD>update<CR>") -- Save the current buffer (file)

map("n", "<leader>q", "<CMD>q<CR>") -- Quit Neovim

map("i", "jk", "<ESC>") -- Exit insert mode

map("n", "<leader>e", "<CMD>Neotree toggle<CR>") -- Toggle file explorer sidebar
map("n", "<leader>r", "<CMD>Neotree focus<CR>") -- Focus the file explorer (if already open)

-- Window Mgmt
map("n", "<leader>o", "<CMD>vsplit<CR>") -- Create vertical split
map("n", "<leader>p", "<CMD>split<CR>") -- Create horizontal split

map("n", "<C-h>", "<C-w>h") -- Move to the window on the left
map("n", "<C-l>", "<C-w>l") -- Move to the window on the right
map("n", "<C-k>", "<C-w>k") -- Move to the window above
map("n", "<C-j>", "<C-w>j") -- Move to the window below

map("n", "<C-Left>", "<C-w><") -- Decrease window width
map("n", "<C-Right>", "<C-w>>") -- Increase window width
map("n", "<C-Up>", "<C-w>+") -- Increase window height
map("n", "<C-Down>", "<C-w>-") -- Decrease window height
