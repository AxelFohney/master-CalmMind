# MasterCalmMind

A strategic guessing game based on Pokémon type effectiveness mechanics, inspired by the classic Mastermind game.

## 🎮 Game Overview

In this game, the computer selects a random combination of Pokémon types. Your challenge is to guess this combination by submitting your own type combinations and analyzing the feedback based on type effectiveness.

Unlike traditional Mastermind where you get feedback on color position and matching, this game provides feedback based on the Pokémon type effectiveness chart (ineffective, not very effective, effective, super effective, or exact match).

## 🌟 Features

- **Three difficulty levels:**
  - **Gym Leader:** 4 types to guess, 10 turns, detailed feedback for each type
  - **Elite Four:** 4 types to guess, 20 turns, aggregate feedback
  - **Champion:** 6 types to guess, 25 turns, aggregate feedback

- **Two naming modes:**
  - **Classic:** Standard Pokémon type names (Fire, Water, Electric, etc.)
  - **Alternative:** Goofy aah alternate names (Oven, Wet, Zap, etc.)

- **Intuitive interface:**
  - Click to select types
  - View history of previous guesses
  - Option for random guesses when you're stuck

## 🚀 How to Play

1. **Setup:** Choose your difficulty level and preferred type naming convention
2. **Gameplay:** Select your types for each guess
3. **Feedback:** Analyze the feedback to refine your next guess
4. **Victory:** Successfully guess all types before running out of turns to win!

## 💻 Technical Details

This game is available in two versions:

### Python Version
- Command-line interface
- Requires Python 3.x to run
- Run with: `python pokemon_mastermind.py`

### Web Version
- Single HTML file with embedded JavaScript and CSS
- No dependencies or installation required
- Just open the HTML file in any modern web browser

## 🧠 Strategy Tips

- In Gym Leader mode, pay close attention to the effectiveness of each individual type
- Type matchups follow the official Pokémon type chart
- Look for patterns in the feedback to narrow down possibilities
- Remember that the same type can appear multiple times in the combination

## 🔄 Version History

- v1.0.0: Initial Python command-line version
- v1.1.0: Added web-based version with improved UI

## 📝 License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## 🙏 Acknowledgments

- Inspired by the classic Mastermind board game
- Based on Pokémon type effectiveness mechanics
- Special thanks to Unova fans out there!

---

Feel free to contribute to this project by submitting issues or pull requests!
