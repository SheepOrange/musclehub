{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Capstone Project 1: MuscleHub AB Test"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: Get started with SQL"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Like most businesses, Janet keeps her data in a SQL database.  Normally, you'd download the data from her database to a csv file, and then load it into a Jupyter Notebook using Pandas.\n",
    "\n",
    "For this project, you'll have to access SQL in a slightly different way.  You'll be using a special Codecademy library that lets you type SQL queries directly into this Jupyter notebook.  You'll have pass each SQL query as an argument to a function called `sql_query`.  Each query will return a Pandas DataFrame.  Here's an example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# This import only needs to happen once, at the beginning of the notebook\n",
    "from codecademySQL import sql_query"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>visit_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Karen</td>\n",
       "      <td>Manning</td>\n",
       "      <td>Karen.Manning@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Annette</td>\n",
       "      <td>Boone</td>\n",
       "      <td>AB9982@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Salvador</td>\n",
       "      <td>Merritt</td>\n",
       "      <td>SalvadorMerritt12@outlook.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Martha</td>\n",
       "      <td>Maxwell</td>\n",
       "      <td>Martha.Maxwell@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Andre</td>\n",
       "      <td>Mayer</td>\n",
       "      <td>AndreMayer90@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                          email  gender  \\\n",
       "0      0      Karen   Manning        Karen.Manning@gmail.com  female   \n",
       "1      1    Annette     Boone               AB9982@gmail.com  female   \n",
       "2      2   Salvador   Merritt  SalvadorMerritt12@outlook.com    male   \n",
       "3      3     Martha   Maxwell       Martha.Maxwell@gmail.com  female   \n",
       "4      4      Andre     Mayer         AndreMayer90@gmail.com    male   \n",
       "\n",
       "  visit_date  \n",
       "0     5-1-17  \n",
       "1     5-1-17  \n",
       "2     5-1-17  \n",
       "3     5-1-17  \n",
       "4     5-1-17  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sql_query('''\n",
    "SELECT *\n",
    "FROM visits\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Here's an example where we save the data to a DataFrame\n",
    "df = sql_query('''\n",
    "SELECT *\n",
    "FROM applications\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: Get your dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's get started!\n",
    "\n",
    "Janet of MuscleHub has a SQLite database, which contains several tables that will be helpful to you in this investigation:\n",
    "- `visits` contains information about potential gym customers who have visited MuscleHub\n",
    "- `fitness_tests` contains information about potential customers in \"Group A\", who were given a fitness test\n",
    "- `applications` contains information about any potential customers (both \"Group A\" and \"Group B\") who filled out an application.  Not everyone in `visits` will have filled out an application.\n",
    "- `purchases` contains information about customers who purchased a membership to MuscleHub.\n",
    "\n",
    "Use the space below to examine each table."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>visit_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Karen</td>\n",
       "      <td>Manning</td>\n",
       "      <td>Karen.Manning@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Annette</td>\n",
       "      <td>Boone</td>\n",
       "      <td>AB9982@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Salvador</td>\n",
       "      <td>Merritt</td>\n",
       "      <td>SalvadorMerritt12@outlook.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Martha</td>\n",
       "      <td>Maxwell</td>\n",
       "      <td>Martha.Maxwell@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Andre</td>\n",
       "      <td>Mayer</td>\n",
       "      <td>AndreMayer90@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                          email  gender  \\\n",
       "0      0      Karen   Manning        Karen.Manning@gmail.com  female   \n",
       "1      1    Annette     Boone               AB9982@gmail.com  female   \n",
       "2      2   Salvador   Merritt  SalvadorMerritt12@outlook.com    male   \n",
       "3      3     Martha   Maxwell       Martha.Maxwell@gmail.com  female   \n",
       "4      4      Andre     Mayer         AndreMayer90@gmail.com    male   \n",
       "\n",
       "  visit_date  \n",
       "0     5-1-17  \n",
       "1     5-1-17  \n",
       "2     5-1-17  \n",
       "3     5-1-17  \n",
       "4     5-1-17  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Examine visits here\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM visits\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>fitness_test_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Kim</td>\n",
       "      <td>Walter</td>\n",
       "      <td>KimWalter58@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-07-03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Tom</td>\n",
       "      <td>Webster</td>\n",
       "      <td>TW3857@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Marcus</td>\n",
       "      <td>Bauer</td>\n",
       "      <td>Marcus.Bauer@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Roberta</td>\n",
       "      <td>Best</td>\n",
       "      <td>RB6305@hotmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-07-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Carrie</td>\n",
       "      <td>Francis</td>\n",
       "      <td>CF1896@hotmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-07-05</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                   email  gender  \\\n",
       "0      0        Kim    Walter   KimWalter58@gmail.com  female   \n",
       "1      1        Tom   Webster        TW3857@gmail.com    male   \n",
       "2      2     Marcus     Bauer  Marcus.Bauer@gmail.com    male   \n",
       "3      3    Roberta      Best      RB6305@hotmail.com  female   \n",
       "4      4     Carrie   Francis      CF1896@hotmail.com  female   \n",
       "\n",
       "  fitness_test_date  \n",
       "0        2017-07-03  \n",
       "1        2017-07-02  \n",
       "2        2017-07-01  \n",
       "3        2017-07-02  \n",
       "4        2017-07-05  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Examine fitness_tests here\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM fitness_tests\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>application_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Roy</td>\n",
       "      <td>Abbott</td>\n",
       "      <td>RoyAbbott32@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-08-12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Agnes</td>\n",
       "      <td>Acevedo</td>\n",
       "      <td>AgnesAcevedo1@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-09-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Roberta</td>\n",
       "      <td>Acevedo</td>\n",
       "      <td>RA8063@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-09-15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Darren</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>DAcosta1996@hotmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Vernon</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>VAcosta1975@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-14</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                    email  gender  \\\n",
       "0      0        Roy    Abbott    RoyAbbott32@gmail.com    male   \n",
       "1      1      Agnes   Acevedo  AgnesAcevedo1@gmail.com  female   \n",
       "2      2    Roberta   Acevedo         RA8063@gmail.com  female   \n",
       "3      3     Darren    Acosta  DAcosta1996@hotmail.com    male   \n",
       "4      4     Vernon    Acosta    VAcosta1975@gmail.com    male   \n",
       "\n",
       "  application_date  \n",
       "0       2017-08-12  \n",
       "1       2017-09-29  \n",
       "2       2017-09-15  \n",
       "3       2017-07-26  \n",
       "4       2017-07-14  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Examine applications here\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM applications\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>purchase_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Roy</td>\n",
       "      <td>Abbott</td>\n",
       "      <td>RoyAbbott32@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-08-18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Roberta</td>\n",
       "      <td>Acevedo</td>\n",
       "      <td>RA8063@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-09-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Vernon</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>VAcosta1975@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Darren</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>DAcosta1996@hotmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Dawn</td>\n",
       "      <td>Adkins</td>\n",
       "      <td>Dawn.Adkins@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-08-24</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                    email  gender purchase_date\n",
       "0      0        Roy    Abbott    RoyAbbott32@gmail.com    male    2017-08-18\n",
       "1      1    Roberta   Acevedo         RA8063@gmail.com  female    2017-09-16\n",
       "2      2     Vernon    Acosta    VAcosta1975@gmail.com    male    2017-07-20\n",
       "3      3     Darren    Acosta  DAcosta1996@hotmail.com    male    2017-07-27\n",
       "4      4       Dawn    Adkins    Dawn.Adkins@gmail.com  female    2017-08-24"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Examine purchases here\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM purchases\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'd like to download a giant DataFrame containing all of this data.  You'll need to write a query that does the following things:\n",
    "\n",
    "1. Not all visits in  `visits` occurred during the A/B test.  You'll only want to pull data where `visit_date` is on or after `7-1-17`.\n",
    "\n",
    "2. You'll want to perform a series of `LEFT JOIN` commands to combine the four tables that we care about.  You'll need to perform the joins on `first_name`, `last_name`, and `email`.  Pull the following columns:\n",
    "\n",
    "\n",
    "- `visits.first_name`\n",
    "- `visits.last_name`\n",
    "- `visits.gender`\n",
    "- `visits.email`\n",
    "- `visits.visit_date`\n",
    "- `fitness_tests.fitness_test_date`\n",
    "- `applications.application_date`\n",
    "- `purchases.purchase_date`\n",
    "\n",
    "Save the result of this query to a variable called `df`.\n",
    "\n",
    "Hint: your result should have 5004 rows.  Does it?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     first_name   last_name                          email  gender visit_date  \\\n",
      "0           Kim      Walter          KimWalter58@gmail.com  female     7-1-17   \n",
      "1           Tom     Webster               TW3857@gmail.com    male     7-1-17   \n",
      "2        Edward       Bowen         Edward.Bowen@gmail.com    male     7-1-17   \n",
      "3        Marcus       Bauer         Marcus.Bauer@gmail.com    male     7-1-17   \n",
      "4       Roberta        Best             RB6305@hotmail.com  female     7-1-17   \n",
      "5        Joseph       Foley        JosephFoley81@gmail.com    male     7-1-17   \n",
      "6        Carrie     Francis             CF1896@hotmail.com  female     7-1-17   \n",
      "7        Sharon     William     Sharon.William@outlook.com  female     7-1-17   \n",
      "8        Teresa       Yates           TYates1988@gmail.com  female     7-1-17   \n",
      "9      Salvador    Cardenas        SCardenas1980@gmail.com    male     7-1-17   \n",
      "10         Glen      Barker          GBarker1976@gmail.com    male     7-1-17   \n",
      "11      Valerie       Munoz           VMunoz1998@gmail.com  female     7-1-17   \n",
      "12       Jeremy        Howe            JHowe1982@gmail.com    male     7-1-17   \n",
      "13         Joel       Combs               JC9481@gmail.com    male     7-1-17   \n",
      "14        Oscar      Forbes         Oscar.Forbes@gmail.com    male     7-1-17   \n",
      "15       Darryl      Albert          DAlbert1975@gmail.com    male     7-1-17   \n",
      "16      Armando  Valenzuela  ArmandoValenzuela67@gmail.com    male     7-1-17   \n",
      "17         June       Ayers               JA2612@gmail.com  female     7-1-17   \n",
      "18        Nancy       Morin          Nancy.Morin@gmail.com  female     7-1-17   \n",
      "19     Lorraine     Lindsay               LL3161@gmail.com  female     7-1-17   \n",
      "20        Carla    Guerrero               CG6354@gmail.com  female     7-1-17   \n",
      "21         Gina      Monroe          GMonroe1973@gmail.com  female     7-1-17   \n",
      "22         Andy    Roberson        ARoberson1972@yahoo.com    male     7-1-17   \n",
      "23       Arnold      Madden          AMadden1998@gmail.com    male     7-1-17   \n",
      "24       Norman   Frederick               NF6074@gmail.com    male     7-1-17   \n",
      "25       Morris        Lott               ML9504@gmail.com    male     7-1-17   \n",
      "26         Cory      Gamble          CGamble1983@gmail.com    male     7-1-17   \n",
      "27       Marcus     Gilliam         MGilliam1997@gmail.com    male     7-1-17   \n",
      "28     Clifford     Guthrie     Clifford.Guthrie@gmail.com    male     7-1-17   \n",
      "29        Terry     Merrill       TerryMerrill91@gmail.com    male     7-1-17   \n",
      "...         ...         ...                            ...     ...        ...   \n",
      "4974    Dolores     Nielsen       DNielsen1989@outlook.com  female     9-9-17   \n",
      "4975      Kathy       Drake         KathyDrake58@yahoo.com  female     9-9-17   \n",
      "4976      Misty    Roberson       Misty.Roberson@gmail.com  female     9-9-17   \n",
      "4977     Marian      Daniel      Marian.Daniel@outlook.com  female     9-9-17   \n",
      "4978      Wanda        Snow          WandaSnow93@gmail.com  female     9-9-17   \n",
      "4979     Nathan    Gallegos        NGallegos1993@gmail.com    male     9-9-17   \n",
      "4980     Evelyn      Reeves      Evelyn.Reeves@hotmail.com  female     9-9-17   \n",
      "4981      Kelly        Tate               KT1133@yahoo.com    male     9-9-17   \n",
      "4982     Willie        Mann            WMann1985@gmail.com  female     9-9-17   \n",
      "4983      Ellen       Blake               EB2921@gmail.com  female     9-9-17   \n",
      "4984   Marjorie        Wong            MWong1985@gmail.com  female     9-9-17   \n",
      "4985     Margie      Walton        Margie.Walton@gmail.com  female     9-9-17   \n",
      "4986      Peter    Figueroa               PF2641@gmail.com    male     9-9-17   \n",
      "4987    Clifton        Leon         Clifton.Leon@gmail.com    male     9-9-17   \n",
      "4988     Gordon    Espinoza               GE6498@gmail.com    male     9-9-17   \n",
      "4989       Luis       Horne             LH9941@outlook.com    male     9-9-17   \n",
      "4990    Francis      Durham      FrancisDurham84@gmail.com    male     9-9-17   \n",
      "4991    Suzanne    Humphrey     SuzanneHumphrey4@gmail.com  female     9-9-17   \n",
      "4992      Glenn      Kinney         Glenn.Kinney@gmail.com    male     9-9-17   \n",
      "4993       Jose   Stevenson      JoseStevenson56@gmail.com    male     9-9-17   \n",
      "4994    Gregory        Wong            GWong1970@gmail.com    male     9-9-17   \n",
      "4995       Dean       Mejia               DM7848@gmail.com    male     9-9-17   \n",
      "4996     Sharon        Hahn               SH5322@gmail.com  female     9-9-17   \n",
      "4997       Adam      Grimes          Adam.Grimes@gmail.com    male     9-9-17   \n",
      "4998       Sara      Malone          SMalone1995@gmail.com  female     9-9-17   \n",
      "4999     Rachel     Hensley      RachelHensley38@gmail.com  female     9-9-17   \n",
      "5000       Leon      Harmon          Leon.Harmon@gmail.com    male     9-9-17   \n",
      "5001       Andy       Pratt          AndyPratt27@gmail.com    male     9-9-17   \n",
      "5002      Ruben     Nielsen     RubenNielsen93@hotmail.com    male     9-9-17   \n",
      "5003    Charles      Carver               CC2490@gmail.com    male     9-9-17   \n",
      "\n",
      "     fitness_test_date application_date purchase_date  \n",
      "0           2017-07-03             None          None  \n",
      "1           2017-07-02             None          None  \n",
      "2                 None       2017-07-04    2017-07-04  \n",
      "3           2017-07-01       2017-07-03    2017-07-05  \n",
      "4           2017-07-02             None          None  \n",
      "5                 None             None          None  \n",
      "6           2017-07-05             None          None  \n",
      "7                 None             None          None  \n",
      "8           2017-07-02             None          None  \n",
      "9           2017-07-07       2017-07-06          None  \n",
      "10                None             None          None  \n",
      "11          2017-07-03       2017-07-05    2017-07-06  \n",
      "12          2017-07-06             None          None  \n",
      "13          2017-07-01             None          None  \n",
      "14                None             None          None  \n",
      "15                None             None          None  \n",
      "16                None             None          None  \n",
      "17                None             None          None  \n",
      "18          2017-07-05             None          None  \n",
      "19          2017-07-05             None          None  \n",
      "20          2017-07-03             None          None  \n",
      "21                None             None          None  \n",
      "22          2017-07-05             None          None  \n",
      "23          2017-07-01             None          None  \n",
      "24                None             None          None  \n",
      "25          2017-07-03             None          None  \n",
      "26                None             None          None  \n",
      "27                None             None          None  \n",
      "28          2017-07-04             None          None  \n",
      "29                None             None          None  \n",
      "...                ...              ...           ...  \n",
      "4974        2017-09-14             None          None  \n",
      "4975              None             None          None  \n",
      "4976        2017-09-14             None          None  \n",
      "4977              None             None          None  \n",
      "4978              None             None          None  \n",
      "4979              None             None          None  \n",
      "4980              None             None          None  \n",
      "4981        2017-09-12             None          None  \n",
      "4982        2017-09-11             None          None  \n",
      "4983        2017-09-10             None          None  \n",
      "4984              None             None          None  \n",
      "4985              None             None          None  \n",
      "4986        2017-09-15             None          None  \n",
      "4987        2017-09-12             None          None  \n",
      "4988        2017-09-12             None          None  \n",
      "4989              None             None          None  \n",
      "4990              None             None          None  \n",
      "4991        2017-09-09       2017-09-13    2017-09-18  \n",
      "4992              None             None          None  \n",
      "4993              None             None          None  \n",
      "4994        2017-09-09             None          None  \n",
      "4995        2017-09-13             None          None  \n",
      "4996              None             None          None  \n",
      "4997              None             None          None  \n",
      "4998        2017-09-13             None          None  \n",
      "4999              None             None          None  \n",
      "5000        2017-09-15             None          None  \n",
      "5001        2017-09-15             None          None  \n",
      "5002              None       2017-09-13          None  \n",
      "5003        2017-09-12             None          None  \n",
      "\n",
      "[5004 rows x 8 columns]\n"
     ]
    }
   ],
   "source": [
    "df = sql_query('''\n",
    "SELECT \n",
    "    v.first_name,\n",
    "    v.last_name,\n",
    "    v.email, \n",
    "    v.gender,\n",
    "    v.visit_date, \n",
    "    ft.fitness_test_date,\n",
    "    ap.application_date,\n",
    "    pc.purchase_date\n",
    "FROM visits v\n",
    "    LEFT JOIN fitness_tests ft\n",
    "        ON v.first_name = ft.first_name\n",
    "        AND v.last_name = ft.last_name\n",
    "        AND v.email = ft.email\n",
    "    LEFT JOIN applications ap\n",
    "        ON v.first_name = ap.first_name\n",
    "        AND v.last_name = ap.last_name\n",
    "        AND v.email = ap.email\n",
    "    LEFT JOIN purchases pc\n",
    "        ON v.first_name = pc.first_name\n",
    "        AND v.last_name = pc.last_name\n",
    "        AND v.email = pc.email    \n",
    "WHERE v.visit_date >= '7-1-17'\n",
    "''')\n",
    "print (df)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3: Investigate the A and B groups"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We have some data to work with! Import the following modules so that we can start doing analysis:\n",
    "- `import pandas as pd`\n",
    "- `from matplotlib import pyplot as plt`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We're going to add some columns to `df` to help us with our analysis.\n",
    "\n",
    "Start by adding a column called `ab_test_group`.  It should be `A` if `fitness_test_date` is not `None`, and `B` if `fitness_test_date` is `None`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "AorB = lambda date: 'A' if pd.notnull(date) else 'B'\n",
    "df['ab_test_group'] = df.fitness_test_date.apply(AorB)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's do a quick sanity check that Janet split her visitors such that about half are in A and half are in B.\n",
    "\n",
    "Start by using `groupby` to count how many users are in each `ab_test_group`.  Save the results to `ab_counts`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  ab_test_group  visit_date\n",
      "0             A        2504\n",
      "1             B        2500\n"
     ]
    }
   ],
   "source": [
    "ab_counts = df.groupby('ab_test_group').visit_date.count().reset_index()\n",
    "print (ab_counts)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'll want to include this information in our presentation.  Let's create a pie cart using `plt.pie`.  Make sure to include:\n",
    "- Use `plt.axis('equal')` so that your pie chart looks nice\n",
    "- Add a legend labeling `A` and `B`\n",
    "- Use `autopct` to label the percentage of each group\n",
    "- Save your figure as `ab_test_pie_chart.png`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.pie([2504,2500], autopct = '%0.2f%%', startangle = 90.0)\n",
    "plt.legend(['Group A', 'Group B'])\n",
    "plt.title('Precentage of A and B Test Groups')\n",
    "plt.axis('equal')\n",
    "plt.savefig('ab_test_pie_chart.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Who picks up an application?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Recall that the sign-up process for MuscleHub has several steps:\n",
    "1. Take a fitness test with a personal trainer (only Group A)\n",
    "2. Fill out an application for the gym\n",
    "3. Send in their payment for their first month's membership\n",
    "\n",
    "Let's examine how many people make it to Step 2, filling out an application.\n",
    "\n",
    "Start by creating a new column in `df` called `is_application` which is `Application` if `application_date` is not `None` and `No Application`, otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "ApplyorNot = lambda date: 'Application' if pd.notnull(date) else 'No Application'\n",
    "df['is_application'] = df.application_date.apply(ApplyorNot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, using `groupby`, count how many people from Group A and Group B either do or don't pick up an application.  You'll want to group by `ab_test_group` and `is_application`.  Save this new DataFrame as `app_counts`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  ab_test_group  is_application  visit_date\n",
      "0             A     Application         250\n",
      "1             A  No Application        2254\n",
      "2             B     Application         325\n",
      "3             B  No Application        2175\n"
     ]
    }
   ],
   "source": [
    "app_counts = df.groupby(['ab_test_group','is_application']).visit_date.count().reset_index()\n",
    "print (app_counts)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We're going to want to calculate the percent of people in each group who complete an application.  It's going to be much easier to do this if we pivot `app_counts` such that:\n",
    "- The `index` is `ab_test_group`\n",
    "- The `columns` are `is_application`\n",
    "Perform this pivot and save it to the variable `app_pivot`.  Remember to call `reset_index()` at the end of the pivot!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_application ab_test_group  Application  No Application\n",
      "0                          A          250            2254\n",
      "1                          B          325            2175\n"
     ]
    }
   ],
   "source": [
    "app_pivot = app_counts.pivot(columns = 'is_application',\n",
    "                            index = 'ab_test_group',\n",
    "                            values = 'visit_date').reset_index()\n",
    "print (app_pivot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Define a new column called `Total`, which is the sum of `Application` and `No Application`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_application ab_test_group  Application  No Application  Total\n",
      "0                          A          250            2254   2504\n",
      "1                          B          325            2175   2500\n"
     ]
    }
   ],
   "source": [
    "app_pivot['Total'] = app_pivot['Application'] + app_pivot['No Application']\n",
    "print (app_pivot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculate another column called `Percent with Application`, which is equal to `Application` divided by `Total`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_application ab_test_group  Application  No Application  Total  \\\n",
      "0                          A          250            2254   2504   \n",
      "1                          B          325            2175   2500   \n",
      "\n",
      "is_application  Percent with Application  \n",
      "0                                   9.98  \n",
      "1                                  13.00  \n"
     ]
    }
   ],
   "source": [
    "app_pivot['Percent with Application'] = (100*app_pivot['Application']/app_pivot['Total']).round(2)\n",
    "print (app_pivot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like more people from Group B turned in an application.  Why might that be?\n",
    "\n",
    "We need to know if this difference is statistically significant.\n",
    "\n",
    "Choose a hypothesis tests, import it from `scipy` and perform it.  Be sure to note the p-value.\n",
    "Is this result significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "P-value 0.00096 < 0.05\n",
      "There is a significant difference between Group A and B in application process.\n"
     ]
    }
   ],
   "source": [
    "from scipy.stats import chi2_contingency\n",
    "contingency = [[250,2254],[325,2175]]\n",
    "_,pvalue,_,_ = chi2_contingency(contingency)\n",
    "\n",
    "if pvalue < 0.05:\n",
    "    print (\"P-value %.5f < 0.05\" % pvalue)\n",
    "    print (\"There is a significant difference between Group A and B in application process.\")\n",
    "else:\n",
    "    print (\"P-value %.5f > 0.05\" % pvalue)\n",
    "    print (\"There is no significant difference between Group A and B in application process.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Who purchases a membership?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Of those who picked up an application, how many purchased a membership?\n",
    "\n",
    "Let's begin by adding a column to `df` called `is_member` which is `Member` if `purchase_date` is not `None`, and `Not Member` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "PcorNot = lambda date: 'Member' if pd.notnull(date) else 'Not Member'\n",
    "df['is_member'] = df.purchase_date.apply(PcorNot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, let's create a DataFrame called `just_apps` the contains only people who picked up an application."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "just_apps = df[df.is_application == 'Application']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Now, let's do a `groupby` to find out how many people in `just_apps` are and aren't members from each group.  Follow the same process that we did in Step 4, including pivoting the data.  You should end up with a DataFrame that looks like this:\n",
    "\n",
    "|is_member|ab_test_group|Member|Not Member|Total|Percent Purchase|\n",
    "|-|-|-|-|-|-|\n",
    "|0|A|?|?|?|?|\n",
    "|1|B|?|?|?|?|\n",
    "\n",
    "Save your final DataFrame as `member_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_member ab_test_group  Member  Not Member  Total  Percent Purchase\n",
      "0                     A     200          50    250             80.00\n",
      "1                     B     250          75    325             76.92\n"
     ]
    }
   ],
   "source": [
    "member_pivot = just_apps.groupby(['ab_test_group','is_member']).visit_date.count().reset_index().\\\n",
    "                pivot(columns = 'is_member',\n",
    "                      index = 'ab_test_group',\n",
    "                      values = 'visit_date').reset_index()\n",
    "member_pivot['Total'] = member_pivot['Member'] + member_pivot['Not Member']\n",
    "member_pivot['Percent Purchase'] = (member_pivot['Member']/member_pivot['Total']*100).round(2)\n",
    "print(member_pivot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like people who took the fitness test were more likely to purchase a membership **if** they picked up an application.  Why might that be?\n",
    "\n",
    "Just like before, we need to know if this difference is statistically significant.  Choose a hypothesis tests, import it from `scipy` and perform it.  Be sure to note the p-value.\n",
    "Is this result significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "P-value2 0.43259 > 0.05\n",
      "There is no significant difference between Group A and B in signing up the membership who picked up applications.\n"
     ]
    }
   ],
   "source": [
    "contingency2 = [[200,50],[250,75]]\n",
    "_,pvalue2,_,_ = chi2_contingency(contingency2)\n",
    "\n",
    "if pvalue2 < 0.05:\n",
    "    print (\"P-value2 %.5f < 0.05\" % pvalue2)\n",
    "    print (\"There is a significant difference between Group A and B in signing up the membership who picked up applications.\")\n",
    "else:\n",
    "    print (\"P-value2 %.5f > 0.05\" % pvalue2)\n",
    "    print (\"There is no significant difference between Group A and B in signing up the membership who picked up applications.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Previously, we looked at what percent of people **who picked up applications** purchased memberships.  What we really care about is what percentage of **all visitors** purchased memberships.  Return to `df` and do a `groupby` to find out how many people in `df` are and aren't members from each group.  Follow the same process that we did in Step 4, including pivoting the data.  You should end up with a DataFrame that looks like this:\n",
    "\n",
    "|is_member|ab_test_group|Member|Not Member|Total|Percent Purchase|\n",
    "|-|-|-|-|-|-|\n",
    "|0|A|?|?|?|?|\n",
    "|1|B|?|?|?|?|\n",
    "\n",
    "Save your final DataFrame as `final_member_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_member ab_test_group  Member  Not Member  Total  Percent Purchase\n",
      "0                     A     200        2304   2504              7.99\n",
      "1                     B     250        2250   2500             10.00\n"
     ]
    }
   ],
   "source": [
    "final_member_pivot = df.groupby(['ab_test_group','is_member']).visit_date.count().reset_index().\\\n",
    "                        pivot(columns = 'is_member',\n",
    "                              index = 'ab_test_group',\n",
    "                              values = 'visit_date').reset_index()\n",
    "final_member_pivot['Total'] = final_member_pivot['Member'] + final_member_pivot['Not Member']\n",
    "final_member_pivot['Percent Purchase'] = (final_member_pivot['Member']/final_member_pivot['Total']*100).round(2)\n",
    "print (final_member_pivot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Previously, when we only considered people who had **already picked up an application**, we saw that there was no significant difference in membership between Group A and Group B.\n",
    "\n",
    "Now, when we consider all people who **visit MuscleHub**, we see that there might be a significant different in memberships between Group A and Group B.  Perform a significance test and check."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "P-value3 0.01472 < 0.05\n",
      "There is a significant difference between Group A and B in signing up the membership.\n"
     ]
    }
   ],
   "source": [
    "contingency3 = [[200,2304],[250,2250]]\n",
    "_,pvalue3,_,_ = chi2_contingency(contingency3)\n",
    "\n",
    "if pvalue3 < 0.05:\n",
    "    print (\"P-value3 %.5f < 0.05\" % pvalue3)\n",
    "    print (\"There is a significant difference between Group A and B in signing up the membership.\")\n",
    "else:\n",
    "    print (\"P-value3 %.5f > 0.05\" % pvalue3)\n",
    "    print (\"There is no significant difference between Group A and B in signing up the membership.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5: Summarize the acquisition funel with a chart"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'd like to make a bar chart for Janet that shows the difference between Group A (people who were given the fitness test) and Group B (people who were not given the fitness test) at each state of the process:\n",
    "- Percent of visitors who apply\n",
    "- Percent of applicants who purchase a membership\n",
    "- Percent of visitors who purchase a membership\n",
    "\n",
    "Create one plot for **each** of the three sets of percentages that you calculated in `app_pivot`, `member_pivot` and `final_member_pivot`.  Each plot should:\n",
    "- Label the two bars as `Fitness Test` and `No Fitness Test`\n",
    "- Make sure that the y-axis ticks are expressed as percents (i.e., `5%`)\n",
    "- Have a title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = plt.subplot()\n",
    "plt.bar(app_pivot.ab_test_group , app_pivot['Percent with Application'],color = ['skyblue','forestgreen']),\n",
    "plt.title('Percentage of Vistors who \\nApplied in Group A and B', fontsize=12)\n",
    "ax.set_xticks(range(len(app_pivot.ab_test_group)))\n",
    "ax.set_xticklabels(['Fitness Test','No Fitness Test'])\n",
    "ax.set_yticks(range(0,21,5))\n",
    "ax.set_yticklabels([str(i)+'%' for i in range(0,21,5)])\n",
    "plt.savefig('PofVisitors_applied.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = plt.subplot()\n",
    "plt.bar(member_pivot.ab_test_group, member_pivot['Percent Purchase'],color = ['skyblue','forestgreen'])\n",
    "plt.title('Percentage of Applied Members who \\nPurchased Membership in Group A and B', fontsize=12)\n",
    "ax.set_xticks(range(len(member_pivot.ab_test_group)))\n",
    "ax.set_xticklabels(['Fitness Test','No Fitness Test'])\n",
    "ax.set_yticks(range(0,101,10))\n",
    "ax.set_yticklabels([str(i)+'%' for i in range(0,101,10)])\n",
    "plt.savefig('Pofapplied_purchased.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = plt.subplot()\n",
    "plt.bar(final_member_pivot.ab_test_group, final_member_pivot['Percent Purchase'],color = ['skyblue','forestgreen'])\n",
    "plt.title('Percentage of Visitors who Purchased Membership \\nin Group A and B', fontsize=12)\n",
    "ax.set_xticks(range(len(final_member_pivot.ab_test_group)))\n",
    "ax.set_xticklabels(['Fitness Test','No Fitness Test'])\n",
    "ax.set_yticks(range(0,16,5))\n",
    "ax.set_yticklabels([str(i)+'%' for i in range(0,16,5)])\n",
    "plt.savefig('Pofvisitors_purchased.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
