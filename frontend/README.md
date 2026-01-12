# 🎲 Dice Game (Balut-Style)

A modern, interactive dice game built with Vue 3 and Vite. Roll 5 dice, place your bets, and win based on various winning combinations!

## 🎮 Game Overview

This is a web-based dice game where players:
- Start with an initial balance
- Place bets on each roll
- Roll 5 dice to form winning combinations
- Win multipliers based on the combination achieved

## ✨ Features

- **Real-time Dice Rolling** - Animated dice rolls with smooth transitions
- **Multiple Winning Combinations**:
  - 🎯 **Pair** (2x multiplier)
  - 🏠 **Full House** (3x multiplier)
  - 🎰 **Balut** (4x multiplier) - Five of a kind
  - 📊 **Straight** (5x multiplier)
  - ⚫ **Other** (No win)
- **Dynamic Balance Tracking** - Real-time balance updates
- **Flexible Betting System** - Adjustable bet amounts
- **Responsive Design** - Clean, card-based UI
- **Backend Integration** - RESTful API for game logic

## 🛠️ Technologies Used

- **Vue 3** - Progressive JavaScript framework with Composition API
- **Vite** - Next-generation frontend build tool
- **JavaScript (ES6+)** - Modern JavaScript features
- **CSS3** - Custom styling with grid layout

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- **Node.js** (v14 or higher)
- **npm** (v6 or higher)
- **Backend API** running on port 8000 (or configure custom URL)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone git@github.com:kseniia-maiesh/dice-test.git
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Configure environment variables**
   
   Create a `.env` file in the root directory:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` to set your API URL:
   ```env
   VITE_API_URL=http://127.0.0.1:8000
   ```

## 🎯 Running the Application

### Development Mode
Start the development server with hot-reload:
```bash
npm run dev
```
The application will be available at `http://localhost:5173`

### Production Build
Build the application for production:
```bash
npm run build
```

### Preview Production Build
Preview the production build locally:
```bash
npm run preview
```

## 📁 Project Structure

```
frontend/
├── public/              # Static assets
├── src/
│   ├── assets/          # Images and static files
│   ├── components/      # Vue components
│   │   ├── BalanceDisplay.vue
│   │   ├── BetControls.vue
│   │   ├── DiceDisplay.vue
│   │   └── PriceList.vue
│   ├── composables/     # Reusable composition functions
│   │   └── useGameApi.js
│   ├── constants/       # Game configuration constants
│   │   └── gameConfig.js
│   ├── App.vue          # Root component
│   ├── main.js          # Application entry point
│   └── style.css        # Global styles
├── .env.example         # Environment variables template
├── .gitignore
├── index.html           # HTML entry point
├── package.json         # Project dependencies
├── vite.config.js       # Vite configuration
└── README.md
```

## 🎲 Game Rules

### Winning Combinations

| Combination | Description | Multiplier |
|------------|-------------|------------|
| **Pair** | Two dice showing the same number | 2x |
| **Full House** | Three of a kind + a pair | 3x |
| **Balut** | Five dice showing the same number | 4x |
| **Straight** | Five consecutive numbers (1-2-3-4-5 or 2-3-4-5-6) | 5x |
| **Other** | No winning combination | 0x |

### How to Play

1. **Set Your Bet** - Choose your bet amount (must not exceed your balance)
2. **Roll the Dice** - Click the "Roll" button to roll all 5 dice
3. **Win or Lose** - Your balance updates based on the combination rolled
   - Win = Bet × Multiplier
   - Loss = Your bet is deducted from balance

## 🔌 API Integration

The frontend communicates with a backend API with the following endpoints:

### POST `/init`
Initialize a new game session
- **Response**: `{ balance: number }`

### POST `/roll`
Roll the dice with a bet
- **Request Body**: `{ bet: number }`
- **Response**: 
  ```json
  {
    "dice": [1, 2, 3, 4, 5],
    "combination": "Straight",
    "win": 150,
    "balance": 250
  }
  ```

## 🎨 Component Overview

### `App.vue`
Main application component that orchestrates the game flow and state management.

### `DiceDisplay.vue`
Displays the 5 dice with rolling animation effects.

### `PriceList.vue`
Shows all possible winning combinations and their multipliers, highlighting active wins.

### `BetControls.vue`
Provides bet amount input and the roll button interface.

### `BalanceDisplay.vue`
Shows the player's current balance.

### `useGameApi.js`
Composable for handling API requests with error handling and loading states.

## ⚙️ Configuration

Game settings can be modified in `src/constants/gameConfig.js`:

```javascript
export const DICE_COUNT = 5;                    // Number of dice
export const DEFAULT_BET = 30;                  // Default bet amount
export const ROLL_ANIMATION_DURATION = 1200;    // Animation duration in ms
```

## 🐛 Troubleshooting

### Backend Connection Issues
If you see API errors:
1. Ensure the backend server is running on the configured port
2. Check the `VITE_API_URL` in your `.env` file
3. Verify CORS is enabled on the backend

### Build Errors
If you encounter build issues:
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

## 📝 Development Notes

- Built with Vue 3's Composition API (`<script setup>`)
- Uses Vite's environment variables (prefixed with `VITE_`)
- Implements responsive grid layout for optimal viewing
- Includes error handling and loading states
- Smooth animations for enhanced user experience

## 📄 License

This project is private and proprietary.

## 👤 Author

Kseniia Maiesh

## 🤝 Contributing

This is a private repository. For any questions or issues, please contact the repository owner.

---

**Happy Rolling! 🎲**
