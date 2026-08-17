# Popup-about-caring-for-friends

A Python tool that creates 150 pop-up windows on the screen to show care and greetings to friends. Each window displays different warm messages, randomly distributed on the screen. Press the spacebar to close all windows at once.

- **Batch Pop-ups**: Creates 150 windows at once to create a caring atmosphere;
- **Random Positioning**: Windows are randomly distributed on the screen, minimizing overlap for better visual effect;
- **Personalized Greetings**: Supports custom names to make each message more personal;
- **One-key Exit**: Press the spacebar to close all pop-ups instantly.

## Features

| Feature | Description |
| --- | --- |
| Batch Window Generation | Creates 150 pop-up windows at once, displaying care and greeting messages |
| Random Position Distribution | Windows are randomly positioned across the screen with intelligent overlap reduction |
| Random Background Colors | Each window randomly selects a soft background color for a warmer visual effect |
| Personalized Names | Supports custom names to make greetings more personalized |
| One-key Exit | Press the spacebar to immediately close all pop-ups |

## Technical Implementation

This project is built using Python's tkinter GUI library. The core logic includes:

1. **Window Creation**: Uses `tk.Toplevel()` to create child windows with topmost property
2. **Content Rendering**: Each window displays randomly selected warm messages using Microsoft YaHei font
3. **Position Calculation**: Algorithm calculates random positions ensuring window overlap doesn't exceed 30%
4. **Rendering Optimization**: Uses `update_idletasks()` and `update()` for immediate rendering to avoid display delays
5. **Batch Generation**: Loops to create 150 windows with 0.05 second intervals for sequential display effect

## Install & Usage

1. Clone the repository or download the `main.py` file

```bash
git clone https://github.com/Qiongkura/Popup-about-caring-for-friends.git
cd Popup-about-caring-for-friends
```

2. Run the script

```bash
python main.py
```

3. Wait for the pop-ups to appear one by one, press the spacebar to exit

## Usage Example

```python
# Run the script to see the effect
python main.py
```

After running, 150 warm pop-up windows will appear on the screen one by one, each displaying different caring messages with random background colors.

## Configuration

| Key | Description | Default |
| --- | --- | --- |
| person_name | Custom name to display in greetings | "happy" |
| tips | List of tips, can be modified or extended | 30 built-in warm messages |
| bg_colors | List of background colors, can be customized | 11 built-in soft colors |
| num_windows | Number of pop-up windows to generate | 150 |
| overlap_threshold | Window overlap threshold (0-1) | 0.3 (30%) |

## Testing

No automated tests available. You can manually run the script to observe if the pop-ups display correctly.

## Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/xxx`)
3. Commit your changes (`git commit -m 'feat: add xxx'`)
4. Push to the branch (`git push origin feature/xxx`)
5. Open a Pull Request

## License

This project is licensed under the [MIT](LICENSE) license.

## Contact

- GitHub: https://github.com/Qiongkura
- WeChat: Qiongkura

## Known Limitations

- Only supports Windows system (depends on tkinter)
- Number of pop-ups is fixed at 150, cannot be dynamically adjusted
- Cannot close individual pop-ups, can only close all at once
- Some systems may require administrator privileges to display windows normally

## Related Projects

- This is an independent tool with no related projects