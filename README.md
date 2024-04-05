# SWAYWM-DOTFILE

This repository contains my custom configuration for a desktop environment based on Arch Linux, using SwayWM as window manager and GNOME for the user interface. The customization is inspired by the Catppuccin Macchiato Pink theme, a community cake theme that aims to be a middle ground between low and high contrast themes, perfect for coding, design and more.

## Content

- **SwayWm**: A window manager for Wayland, known for its efficiency and flexibility.
- **GNOME**: A feature-rich user interface that provides a complete user experience.
- **Catppuccin Macchiato Pink Theme**: A soft pastel theme with 26 attractive colors, designed to be pleasing to the eye and comfortable for everyday work.

## Screenshots

<img src="https://github.com/me-hpp/swaywm-dotfile/assets/122117784/33faeef9-a9d2-4966-80ab-75f7dc53212b"/>
<img src="https://github.com/me-hpp/swaywm-dotfile/assets/122117784/43046026-eff5-4263-a644-06bbdf9400b6"/>
<img src="https://github.com/me-hpp/swaywm-dotfile/assets/122117784/e9fa3dc7-8bb7-446f-8236-4d9b5ddf6d88"/>
<img src="https://github.com/me-hpp/swaywm-dotfile/assets/122117784/110811db-7665-4164-a796-240c0761caba"/>
<img src="https://github.com/me-hpp/swaywm-dotfile/assets/122117784/8ab899ce-5d58-446b-b329-2c3fe084861d"/>
<img src="https://github.com/me-hpp/swaywm-dotfile/assets/122117784/7b682cc0-e6f1-44a8-814c-3ed100fab897"/>
<img src="https://github.com/me-hpp/swaywm-dotfile/assets/122117784/7f6334c1-ee99-4b78-95a4-8a9da3ec5e64"/>

## Installing the Catppuccin Macchiato Pink Theme

To install the Catppuccin Macchiato Pink theme on Arch Linux, you can use the following command:
`yay -S catppuccin-gtk-theme-macchiato`

## Documentations

Here you can find all the necessary that you need to have on your desktop before proceeding.

- [Alacritty](https://github.com/alacritty/alacritty/blob/master/INSTALL.md)
- [Cava](https://github.com/karlstav/cava)
- [Cowsay](https://github.com/piuccio/cowsay)
- [Flameshot](https://aur.archlinux.org/flameshot-git.git)
- [Kitty](https://github.com/kovidgoyal/kitty/)
- [Neofetch](https://github.com/dylanaraps/neofetch)
- [Nvim](https://github.com/neovim/neovim/blob/master/INSTALL.md)
- [P10K](https://github.com/romkatv/powerlevel10k)
- [Pipes.sh](https://github.com/pipeseroni/pipes.sh)
- [Rofi](https://github.com/davatorium/rofi/blob/next/INSTALL.md)
- [Spicetify](https://spicetify.app/docs/advanced-usage/installation/)
- [SwayWm](https://github.com/swaywm/sway)
- [Waybar](https://github.com/Alexays/Waybar)
- [Zsh](https://github.com/ohmyzsh/ohmyzsh)

## Installations

Follow this steps

```
git clone https://github.com/me-hpp/swaywm-dotfile.git
cd swaywm-dotfile
cp -r config/* ~/.config/
cp -r local/* ~/.local/share/
mkdir ~/.themes
cp -r .themes/* ~/.themes
cp -r .zshrc ~
sudo cp -r usr/share/backgrounds/sway/* /usr/share/backgrounds/sway/
```

## Important Keyboard Shortcuts

Here is a list of the most important keyboard shortcuts used in this SwayWM configuration. These shortcuts facilitate navigation and window management in your desktop environment.

### Window Navigation and Management

- **Launch Terminal**: `$mod+Return`
- **Kill Focused Window**: `$mod+Shift+q`
- **Launch Launcher**: `$mod+d`
- **Move Focused Window**: `$mod+Shift+$left`, `$mod+Shift+$down`, `$mod+Shift+$up`, `$mod+Shift+$right`
- **Switch Window Modes**: `$mod+Shift+space`
- **Reload Configuration**: `$mod+Shift+c`
- **Exit Sway**: `$mod+Shift+e`

### Workspace Navigation

- **Switch to Workspace**: `$mod+1`, `$mod+2`, ..., `$mod+0`
- **Move Window to Workspace**: `$mod+Shift+1`, `$mod+Shift+2`, ..., `$mod+Shift+0`

### Layout Management

- **Split Window Horizontally**: `$mod+b`
- **Split Window Vertically**: `$mod+v`
- **Switch Layout**: `$mod+s` for stacking, `$mod+w` for tabbed, `$mod+e` for toggle split
- **Make Focused Window Full Screen**: `$mod+f`

### SwayWM Configuration

- **Output Configuration**: `output * bg /usr/share/backgrounds/sway/2.png fill`
- **Idle Configuration**: `exec swayidle -w timeout 300 'swaylock -f -c 000000' timeout 600 'swaymsg "output * power off"' resume 'swaymsg "output * power on"' before-sleep 'swaylock -f -c 000000'`

### Specific Tools and Applications

- **Flameshot**: `$mod+p` for screenshot
- **Network Management**: `$mod+Shift+n` to start NetworkManager

## Important Aliases

Here is a list of the most important aliases used in this configuration. These aliases facilitate the execution of common and custom commands.

### System Commands

- **`ginit`**: Initializes a Git repository, creates a README.md, and a .gitignore.
- **`update`**: Updates the system.

### Git Commands

- **`ginit`**: Initializes a Git repository, creates a README.md, and a .gitignore.

### Arch Linux Commands

- **`update`**: Updates the system.
- **`install`**: Installs a package.
- **`remove`**: Removes a package.

### Navigation and Search Commands

- **`ls`**: Lists files.
- **`la`**: Lists files in detail.
- **`hi`**: Shows command history.
- **`hg`**: Searches command history.

### Tools and Applications

- **`vim`**: Opens the Neovim editor.
- **`pi`**: Opens Pipes.sh.
- **`tty`**: Opens TTY Clock.
- **`ca`**: Opens Cava (audio visualizer).

## Related

Here are some related projects

[Catppuccin](https://github.com/catppuccin/catppuccin)

## Authors

- [@me-hpp](https://www.github.com/me-hpp)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contributing

Contributions are always welcome!

## FAQ

#### Does it work on ubuntu?

I have not tested it, but most probably yes, you just have to configure some parameters.

#### Can I modify it my way?

Yes, you can completely modify it to your style.
