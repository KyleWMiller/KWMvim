# KWMvim ✨ - My Slightly Opinionated Neovim Setup

[![Lua](https://img.shields.io/badge/Made%20with-Lua-blueviolet.svg?style=for-the-badge&logo=lua)](https://lua.org)
[![Neovim](https://img.shields.io/badge/Neovim-0.9%2B-green.svg?style=for-the-badge&logo=neovim)](https://neovim.io/)

So, you stumbled upon my Neovim config? Cool, cool. 😎

This isn't just _any_ config; it's **KWMvim**. It's my personal command center, meticulously crafted (read: constantly tweaked and occasionally broken) in Lua. It's built with [Lazy.nvim](https://github.com/folke/lazy.nvim) because, honestly, who has time for slow plugin managers?

Think of it as a comfy, supercharged workspace primarily tuned for **Web Dev** (JS, TS, HTML, CSS) and **Rust**, but it plays nice with other stuff too.

## 🤔 Why Tho?

- **Speed:** Because waiting for your editor is _so_ last decade. Lazy loading keeps things snappy.
- **Lua is Fun:** Migrating from Vimscript felt like upgrading from a dial-up modem.
- **Looks Matter:** Rocking the gorgeous [Kanagawa](https://github.com/rebelot/kanagawa.nvim) theme. Easy on the eyes, tough on the code.
- **Sensible Defaults (for me):** Things are set up _just_ how I like 'em. Tabs are spaces (4 wide, fight me), relative numbers are off (yeah, I said it), and the clipboard just _works_.

## 🚀 Core Features & Fan Favorites

This setup is packed, but here are some highlights managed by the magic of `lazy.nvim`:

- **Navigation & Search:**
  - [**Telescope.nvim**](https://github.com/nvim-telescope/telescope.nvim): Fuzzy finding everything. Files (`<leader>ff`), Grep (`<leader>fg`), Buffers (`<leader>fb`), Git Status (`<leader>fs`) - it's the CTRL+P killer you deserve.
  - [**Neo-tree.nvim**](https://github.com/nvim-neo-tree/neo-tree.nvim): A file explorer that doesn't suck. Toggle with `<leader>e`.
- **Coding Power-Ups:**
  - [**Nvim-Treesitter**](https://github.com/nvim-treesitter/nvim-treesitter): Smarter syntax highlighting, indentation, and more. Makes code look pretty _and_ understandable. Includes `nvim-ts-autotag` for HTML/XML bliss.
  - [**Nvim-Cmp**](https://github.com/hrsh7th/nvim-cmp): Autocompletion that actually helps, powered by LSP, snippets, buffers, and paths.
  - [**Conform.nvim**](https://github.com/stevearc/conform.nvim): Auto-formatting on save using `prettier`, `stylua`, `isort`, `black`, etc. Keepin' it clean.
  - [**Nvim-Autopairs**](https://github.com/windwp/nvim-autopairs): Closes brackets and quotes for you. Simple, yet essential.
- **Git Integration:**
  - [**Gitsigns.nvim**](https://github.com/lewis6991/gitsigns.nvim): Git diff markers directly in the sign column. See changes without leaving your flow.
- **Language Specific:**
  - [**Rustaceanvim**](https://github.com/mrcjkb/rustaceanvim) & [**Crates.nvim**](https://github.com/Saecki/crates.nvim): Making Rust development feel first-class.
- **UI Candy:**
  - [**Lualine.nvim**](https://github.com/nvim-lualine/lualine.nvim): A statusline that's both informative and sleek.
  - [**Which-Key.nvim**](https://github.com/folke/which-key.nvim): Helps you remember all those leader keybindings. Press `<leader>` and wait a sec.
  - [**Nvim-Colorizer.lua**](https://github.com/norcalli/nvim-colorizer.lua): Shows hex colors inline. Pretty neat.
  - [**Toggleterm.nvim**](https://github.com/akinsho/toggleterm.nvim): Quick access to a floating terminal (`<F7>`).

## ✨ Keybinding Sneak Peek

- `mapleader` is `<Space>` (obviously).
- `jk` in Insert mode escapes back to Normal mode (the superior way).
- Window splits: `<leader>o` (vertical), `<leader>p` (horizontal).
- Window navigation: `<C-h/j/k/l>`.
- Check `lua/kmill/maps.lua` for the full list!

## 🛠️ Installation (If You Dare)

1.  Make sure you have Neovim v0.9 or later.
2.  Backup your existing `~/.config/nvim` directory (seriously, do it).
3.  Clone this repo: `git clone https://github.com/KyleWMiller/KWMvim.git ~/.config/nvim`
4.  Launch `nvim`. `Lazy.nvim` should bootstrap itself and install plugins.
5.  Restart `nvim` just for good measure.
6.  Run `:Mason` to check LSP/formatter/linter installations if needed.

## 📜 Disclaimer

This is _my_ setup. It changes. Sometimes often. Sometimes drastically. Use it as inspiration, steal bits you like, or fork it and make it your own. If it breaks, you get to keep both pieces! 😉

Happy Vimming!
