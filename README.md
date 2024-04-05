# SWAYWM-DOTFILE

This repository contains my custom configuration for a desktop environment based on Arch Linux, using SwayWM as window manager and GNOME for the user interface. The customization is inspired by the Catppuccin Macchiato Pink theme, a community cake theme that aims to be a middle ground between low and high contrast themes, perfect for coding, design and more.

## Content

- **SwayWm**: A window manager for Wayland, known for its efficiency and flexibility.
- **GNOME**: A feature-rich user interface that provides a complete user experience.
- **Catppuccin Macchiato Pink Theme**: A soft pastel theme with 26 attractive colors, designed to be pleasing to the eye and comfortable for everyday work.

## Installing the Catppuccin Macchiato Pink Theme

To install the Catppuccin Macchiato Pink theme on Arch Linux, you can use the following command:
```yay -S catppuccin-gtk-theme-macchiato```

## Documentations

Here you can find all the necessary applications that you need to have on your desktop before proceeding.

[Alacritty] (https://github.com/alacritty/alacritty/blob/master/INSTALL.md)
[Cava] (https://github.com/karlstav/cava)
[Flameshot] (https://aur.archlinux.org/flameshot-git.git)
[Kitty] (https://github.com/kovidgoyal/kitty/)
[Neofetch] (https://github.com/dylanaraps/neofetch)
[Nvim] (https://github.com/neovim/neovim/blob/master/INSTALL.md)
[P10K] (https://github.com/romkatv/powerlevel10k)
[Rofi] (https://github.com/davatorium/rofi/blob/next/INSTALL.md)
[Spicetify] (https://spicetify.app/docs/advanced-usage/installation/)
[SwayWm] (https://github.com/swaywm/sway)
[Waybar] (https://github.com/Alexays/Waybar)
[Zsh] (https://github.com/ohmyzsh/ohmyzsh)

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

## Screenshots

<img src="https://github.com/me-hpp/swaywm-dotfile/assets/122117784/33faeef9-a9d2-4966-80ab-75f7dc53212b"/>
<img src="https://github.com/me-hpp/swaywm-dotfile/assets/122117784/43046026-eff5-4263-a644-06bbdf9400b6"/>
<img src="https://github.com/me-hpp/swaywm-dotfile/assets/122117784/e9fa3dc7-8bb7-446f-8236-4d9b5ddf6d88"/>
<img src="https://github.com/me-hpp/swaywm-dotfile/assets/122117784/110811db-7665-4164-a796-240c0761caba"/>
<img src="https://github.com/me-hpp/swaywm-dotfile/assets/122117784/8ab899ce-5d58-446b-b329-2c3fe084861d"/>
<img src="https://github.com/me-hpp/swaywm-dotfile/assets/122117784/7b682cc0-e6f1-44a8-814c-3ed100fab897"/>
<img src="https://github.com/me-hpp/swaywm-dotfile/assets/122117784/7f6334c1-ee99-4b78-95a4-8a9da3ec5e64"/>

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
