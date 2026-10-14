# Deepwick for Konsole

A deep navy terminal color scheme with Visual Studio 2022's syntax colors.

> Deepwick is an unofficial theme derived from
> [Polywick Blue](https://vscode.polywickstudio.net) by Polywick Studio (MIT).
> Not affiliated with Polywick Studio.

![Deepwick in Konsole](screenshot.png)

## Install

```sh
mkdir -p "${XDG_DATA_HOME:-$HOME/.local/share}/konsole"
cp Deepwick.colorscheme "${XDG_DATA_HOME:-$HOME/.local/share}/konsole/"
```

## Activate

**Settings → Edit Current Profile… → Appearance**, choose **Deepwick**, then
**OK**. To try it without changing a profile:

```sh
konsole -p ColorScheme=Deepwick
```

## Notes

- Faint and intense backgrounds and foregrounds use the normal colors; bold
  text is not brightened.

Tested with Konsole 26.08.1.

## License

MIT. See [LICENSE](LICENSE).
