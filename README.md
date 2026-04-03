# Project-20

## 🏓 Pong Game

A classic two-player Pong game built with Python's Turtle graphics library.

## 📋 Description

Play the classic arcade game Pong against a friend! Control paddles to hit the ball back and forth. First player to miss loses a point!

## 🎮 How to Play

### Controls

**Player 1 (Left Paddle - Red Side):**
- `W` - Move up
- `S` - Move down

**Player 2 (Right Paddle - Blue Side):**
- `↑ Up Arrow` - Move up
- `↓ Down Arrow` - Move down

## 🎯 Game Rules

- Hit the ball with your paddle to send it back to your opponent
- If the ball passes your paddle, your opponent scores a point
- The ball speeds up slightly each time it bounces off a paddle
- Score is displayed at the top of the screen
- Play continues indefinitely - first to rage quit loses! 😄

## 🚀 Installation & Setup

### Prerequisites

- Python 3.x installed on your system
- Turtle graphics library (comes pre-installed with Python)

### Installation

1. Clone or download this repository
2. Ensure all files are in the same directory:
   - `main.py`
   - `paddle.py`
   - `ball.py`
   - `scoreboard.py`

### Running the Game
```bash
python main.py
```

Or on some systems:
```bash
python3 main.py
```

## 📁 File Structure
```
pong-game/
│
├── main.py          # Main game loop and collision detection
├── paddle.py        # Paddle class (movement and boundaries)
├── ball.py          # Ball class (movement, bouncing, speed)
└── scoreboard.py    # Scoreboard class (score tracking and display)
```

## 🛠️ Technical Details

### Game Configuration

- **Screen Size**: 1000 x 600 pixels
- **Background**: Black
- **Game Speed**: 0.1 seconds per frame
- **Paddle Color**: White
- **Ball Color**: Blue
- **Score Display**: White text (80pt bold Arial)

### Game Mechanics

- **Ball Speed**: Starts at 10 pixels/frame
- **Speed Increase**: 10% faster after each paddle hit
- **Paddle Movement**: 40 pixels per key press
- **Collision Distance**: 50 pixels from paddle center

## 🎨 Customization

You can customize the game by modifying constants in the files:

**main.py:**
```python
SCREEN_WIDTH = 1000           # Screen width
SCREEN_HEIGHT = 600           # Screen height
GAME_SPEED = 0.1              # Game speed (lower = faster)
COLLISION_DISTANCE = 50       # Paddle collision sensitivity
```

**ball.py:**
```python
BASE_SPEED = 10               # Starting ball speed
SPEED_MULTIPLIER = 1.1        # Speed increase per hit (1.1 = 10% faster)
```

**paddle.py:**
```python
MOVE_DISTANCE = 40            # Paddle movement distance
UPPER_BOUNDARY = 260          # Top boundary
LOWER_BOUNDARY = -260         # Bottom boundary
```

## 🐛 Known Issues

The ball may do a 'ghost bounce' when the paddle is near a wall.

## 🔮 Future Enhancements

Potential improvements for future versions:

- [ ] AI opponent (single-player mode)
- [ ] Sound effects
- [ ] Win condition (first to X points)
- [ ] Pause functionality
- [ ] Difficulty levels
- [ ] Power-ups
- [ ] Different ball types/speeds
- [ ] Custom paddle colors

## 📝 Code Structure

### Classes

**Paddle** (`paddle.py`)
- Creates and positions paddles
- Handles up/down movement
- Enforces boundary limits

**Ball** (`ball.py`)
- Manages ball position and movement
- Handles wall bounces
- Increases speed after paddle hits
- Resets position after scoring

**Scoreboard** (`scoreboard.py`)
- Tracks scores for both players
- Displays scores at top of screen
- Draws center dividing line

## 🎓 Learning Concepts

This project demonstrates:

- Object-Oriented Programming (OOP)
- Class inheritance (Turtle graphics)
- Game loop implementation
- Collision detection
- Event handling (keyboard input)
- Modular code organization
- Game physics (bouncing, acceleration)

## 👥 Players

This is a **two-player local multiplayer game**. Grab a friend and see who wins!

## 👨‍💻 Author

Created as a Python learning project using Turtle graphics.

## 📄 License

Free to use and modify for educational purposes.

## 🙏 Acknowledgments

- Built with Python's Turtle graphics library
- Inspired by the classic Atari Pong game (1972)

---

**Enjoy the game! 🏓🎮**

*Pro tip: The ball gets faster the longer the rally goes. Good luck!*
