# Cooking Django App

A web-based application for sharing and discovering recipes, built using Django and Docker. This app allows users to browse, create, and share their favorite recipes with an easy-to-use interface.

# Features

### Recipe Management

- **Create, update, and delete recipes**: Easily manage your personal recipe collection.

- **Categorization**: Organize recipes by categories such as Breakfast, Lunch, Dinner, etc.

### Shopping List

- **Create shopping** lists: Add ingredients from recipes to your shopping list.

- **Download lists**: Export your shopping list as a CSV file for easy access.


# Installation

### Clone the Repository

```bash
git clone https://github.com/ehaligow/cookingDjangoApp.git
cd cookingDjangoApp
```

### Build and Start the Application

```bash
make buildAndRun
```
### Apply Database Migrations

```bash
make migrations
```

### Access the Application

Visit http://127.0.0.1:8000 in your web browser.