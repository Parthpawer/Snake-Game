
    <title>Snake Game with Turtle Graphics</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #282c34;
            color: white;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        main {
            text-align: center;
        }

        h1 {
            color: #61dafb;
        }

        p {
            font-size: 1.2em;
            line-height: 1.6;
        }

        code {
            background-color: #282c34;
            color: #61dafb;
            padding: 2px 4px;
            font-size: 0.9em;
            border-radius: 4px;
        }

        a {
            color: #61dafb;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        pre {
            background-color: #1e1e1e;
            padding: 10px;
            border-radius: 6px;
            overflow-x: auto;
        }
    </style>



        <h1>Snake Game with Turtle Graphics</h1>
        <p>This is a simple Snake Game built using Python and the Turtle graphics library. The game consists of a snake controlled by the arrow keys, with the goal of collecting red food items to grow longer. The snake must avoid colliding with the screen edges and itself.</p>

        <h2>Files</h2>
        <ul>
            <li><code>main.py</code>: The main entry point for the Snake Game.</li>
            <li><code>snake.py</code>: Defines the <code>Snake</code> class, responsible for the snake's behavior and movement.</li>
            <li><code>food.py</code>: Implements the <code>Food</code> class, representing the red food items that the snake must eat to grow.</li>
            <li><code>score.py</code>: Contains the <code>Scoreboard</code> class, handling the game score.</li>
        </ul>

        <h2>Usage</h2>
        <ol>
            <li>Ensure you have Python installed on your machine.</li>
            <li>Run <code>main.py</code> to start the Snake Game.</li>
            <li>Control the snake's direction using the arrow keys.</li>
            <li>Collect red food items to increase your score.</li>
            <li>The game ends if the snake collides with the screen edges or itself.</li>
        </ol>

        <h2>Dependencies</h2>
        <ul>
            <li>Python 3.x</li>
            <li>Turtle Graphics Library</li>
        </ul>

        <h2>Credits</h2>
        <ul>
            <li>Game developed by [Your Name]</li>
            <li>Inspired by classic Snake Games</li>
        </ul>

