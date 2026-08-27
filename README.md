
 # RateGuin
   #### Video Demo: <URL HERE>

   #### Description:

   RateGuin was born from a personal passion: aggregating ratings and reviews for all the media I consume into one single place.

   As someone who loves taking notes, tracking progress, and creating lists of books, movies, series, and games,
   I found myself constantly bouncing between multiple fragmented platforms—like Metacritic, Goodreads, and How Long to Beat.
   To solve this, I decided to build a centralized terminal application where I could combine all of these records into a single dashboard.

   ## How It Works

   ### 1. The Welcome Screen
   When you launch the program, an ASCII Penguin greets you and displays the Main Menu.
   From there, you can choose which entertainment category you want to manage, access the Help section, or Quit the application.

   You operate the Main Menu by entering a number from 1 to 5, as indicated in the options list.
   If your input is invalid or not a number, the program catches the error, prints a brief instruction, and prompts you again.
   *  **Help** (4) prompts the Penguin to explain the programs's usage.
   *  **Quit** (5) safely terminates the program with a goodbye message.
   *  Options 1, 2, and 3 redirect you to the lists and submenus for **Books**, **Movies/Series**, or **Games**, respectively.

   Any prompt you choose will clear the terminal and print something new, to keep it clean and give you the idea of continuity.

   ### 2. Program Structure and Data Persistence
   The core of the application is driven by two main classes: **Menu** and **Functions**.
   * **Menu Class:** Manages the main execution loop, keeping the program running and continuously prompting the user for commands.
   * **Function Class:** Coordinates all core operations, handling every CRUD feature alongside extra utilities like sorting, filtering, and exiting.
   Additionally, this class manages initialization by verifying if all the three **.csv** storage files exist (books.csv, movies.csv, games.csv) and creating them automatically if they are missing.

   ### 3. The Submenu (CRUD Operations)
   After choosing a category to view or edit, the program clears the terminal and renders the current data table. Directly underneath this list, a contextual submenu prompts you for an action string. If your input is invalid, the system catches the error, displays an instructional message, and reprompts you.

   The available actions are:
   * **Home**: Clears the terminal and returns you to the Main Menu.
   * **Add**: Initiates a sequential series of prompts to guide you through adding a new item (the name attribute is strictly mandatory).
   * **Edit**: Prompts for the specific ID of the item you want to modify, asks which attribute you wish to change, and updates it.
   * **Del**: Prompts for the item ID you want to remove and requests an explicit confirmation (Yes/No) before deletion.
   * **Sort**: Allows you to dynamically sort the table by any core attribute (except for the long text in review).
   * **Filter**: Filters the list based on specific criteria. In its current state, it is highly optimized for isolating your **Favorites**.
   * **Quit**: Safely exits the entire application directly from the submenu.

   ### 4. General Attributes (Object-Oriented Architecture)
   All media items share a core set of foundational properties managed by a parent class called *Art*:
   * **Name** (String, strictly mandatory)
   * **Rating** (Numeric score, which automatically converts commas "," to dots "." for compatibility)
   * **Date Completed** (Enforces strict Date formatting)
   * **Review/Notes** (Text)
   * **Favorite Status** (Yes/No)

   Inside the Art superclass, custom getters and setters handle input validation to guarantee data integrity.
   Additionally, I implemented a centralized prompt attribute within the class.
   This allows the program to loop through and pull specific questions for each field automatically, keeping the code clean and facilitating future translations.

   ### 5. Specific Attributes (Subclasses)
   To capture the unique aspects of each medium, the project leverages inheritance through specialized subclasses:
   * **Books:** Tracks page count and author.
   * **Movies & Series:** Tracks duration and director.
   * **Games:** Tracks hours played, platform, and development studio.
