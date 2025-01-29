{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a15fe6e3-0100-405c-8b08-d597a381c973",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "02ca7888-6629-428f-9522-3bf1e3ddb688",
   "metadata": {},
   "outputs": [],
   "source": [
    "data=pd.read_excel('Rice_Cammeo_Osmancik.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7de3ff91-4a3a-475a-9e3a-00c1e3c7b3cc",
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
       "      <th>Area</th>\n",
       "      <th>Perimeter</th>\n",
       "      <th>Major_Axis_Length</th>\n",
       "      <th>Minor_Axis_Length</th>\n",
       "      <th>Eccentricity</th>\n",
       "      <th>Convex_Area</th>\n",
       "      <th>Extent</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>15231</td>\n",
       "      <td>525.578979</td>\n",
       "      <td>229.749878</td>\n",
       "      <td>85.093788</td>\n",
       "      <td>0.928882</td>\n",
       "      <td>15617</td>\n",
       "      <td>0.572896</td>\n",
       "      <td>Cammeo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>14656</td>\n",
       "      <td>494.311005</td>\n",
       "      <td>206.020065</td>\n",
       "      <td>91.730972</td>\n",
       "      <td>0.895405</td>\n",
       "      <td>15072</td>\n",
       "      <td>0.615436</td>\n",
       "      <td>Cammeo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>14634</td>\n",
       "      <td>501.122009</td>\n",
       "      <td>214.106781</td>\n",
       "      <td>87.768288</td>\n",
       "      <td>0.912118</td>\n",
       "      <td>14954</td>\n",
       "      <td>0.693259</td>\n",
       "      <td>Cammeo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>13176</td>\n",
       "      <td>458.342987</td>\n",
       "      <td>193.337387</td>\n",
       "      <td>87.448395</td>\n",
       "      <td>0.891861</td>\n",
       "      <td>13368</td>\n",
       "      <td>0.640669</td>\n",
       "      <td>Cammeo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>14688</td>\n",
       "      <td>507.166992</td>\n",
       "      <td>211.743378</td>\n",
       "      <td>89.312454</td>\n",
       "      <td>0.906691</td>\n",
       "      <td>15262</td>\n",
       "      <td>0.646024</td>\n",
       "      <td>Cammeo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3805</th>\n",
       "      <td>11441</td>\n",
       "      <td>415.858002</td>\n",
       "      <td>170.486771</td>\n",
       "      <td>85.756592</td>\n",
       "      <td>0.864280</td>\n",
       "      <td>11628</td>\n",
       "      <td>0.681012</td>\n",
       "      <td>Osmancik</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3806</th>\n",
       "      <td>11625</td>\n",
       "      <td>421.390015</td>\n",
       "      <td>167.714798</td>\n",
       "      <td>89.462570</td>\n",
       "      <td>0.845850</td>\n",
       "      <td>11904</td>\n",
       "      <td>0.694279</td>\n",
       "      <td>Osmancik</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3807</th>\n",
       "      <td>12437</td>\n",
       "      <td>442.498993</td>\n",
       "      <td>183.572922</td>\n",
       "      <td>86.801979</td>\n",
       "      <td>0.881144</td>\n",
       "      <td>12645</td>\n",
       "      <td>0.626739</td>\n",
       "      <td>Osmancik</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3808</th>\n",
       "      <td>9882</td>\n",
       "      <td>392.296997</td>\n",
       "      <td>161.193985</td>\n",
       "      <td>78.210480</td>\n",
       "      <td>0.874406</td>\n",
       "      <td>10097</td>\n",
       "      <td>0.659064</td>\n",
       "      <td>Osmancik</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3809</th>\n",
       "      <td>11434</td>\n",
       "      <td>404.709991</td>\n",
       "      <td>161.079269</td>\n",
       "      <td>90.868195</td>\n",
       "      <td>0.825692</td>\n",
       "      <td>11591</td>\n",
       "      <td>0.802949</td>\n",
       "      <td>Osmancik</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3810 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       Area   Perimeter  Major_Axis_Length  Minor_Axis_Length  Eccentricity  \\\n",
       "0     15231  525.578979         229.749878          85.093788      0.928882   \n",
       "1     14656  494.311005         206.020065          91.730972      0.895405   \n",
       "2     14634  501.122009         214.106781          87.768288      0.912118   \n",
       "3     13176  458.342987         193.337387          87.448395      0.891861   \n",
       "4     14688  507.166992         211.743378          89.312454      0.906691   \n",
       "...     ...         ...                ...                ...           ...   \n",
       "3805  11441  415.858002         170.486771          85.756592      0.864280   \n",
       "3806  11625  421.390015         167.714798          89.462570      0.845850   \n",
       "3807  12437  442.498993         183.572922          86.801979      0.881144   \n",
       "3808   9882  392.296997         161.193985          78.210480      0.874406   \n",
       "3809  11434  404.709991         161.079269          90.868195      0.825692   \n",
       "\n",
       "      Convex_Area    Extent     Class  \n",
       "0           15617  0.572896    Cammeo  \n",
       "1           15072  0.615436    Cammeo  \n",
       "2           14954  0.693259    Cammeo  \n",
       "3           13368  0.640669    Cammeo  \n",
       "4           15262  0.646024    Cammeo  \n",
       "...           ...       ...       ...  \n",
       "3805        11628  0.681012  Osmancik  \n",
       "3806        11904  0.694279  Osmancik  \n",
       "3807        12645  0.626739  Osmancik  \n",
       "3808        10097  0.659064  Osmancik  \n",
       "3809        11591  0.802949  Osmancik  \n",
       "\n",
       "[3810 rows x 8 columns]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cd1e42d6-34b2-486c-a598-915f1940f38d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Area                 0\n",
       "Perimeter            0\n",
       "Major_Axis_Length    0\n",
       "Minor_Axis_Length    0\n",
       "Eccentricity         0\n",
       "Convex_Area          0\n",
       "Extent               0\n",
       "Class                0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ba25f07b-b0a4-4bdf-8553-b59a76df3603",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "256d6e21-0d70-47b5-af28-d587447f0c9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=data.drop(['Class'],axis=1)\n",
    "y=data['Class']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "64f791f9-dd71-4a8d-8585-8b881a6982b7",
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
       "      <th>Area</th>\n",
       "      <th>Perimeter</th>\n",
       "      <th>Major_Axis_Length</th>\n",
       "      <th>Minor_Axis_Length</th>\n",
       "      <th>Eccentricity</th>\n",
       "      <th>Convex_Area</th>\n",
       "      <th>Extent</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>15231</td>\n",
       "      <td>525.578979</td>\n",
       "      <td>229.749878</td>\n",
       "      <td>85.093788</td>\n",
       "      <td>0.928882</td>\n",
       "      <td>15617</td>\n",
       "      <td>0.572896</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>14656</td>\n",
       "      <td>494.311005</td>\n",
       "      <td>206.020065</td>\n",
       "      <td>91.730972</td>\n",
       "      <td>0.895405</td>\n",
       "      <td>15072</td>\n",
       "      <td>0.615436</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>14634</td>\n",
       "      <td>501.122009</td>\n",
       "      <td>214.106781</td>\n",
       "      <td>87.768288</td>\n",
       "      <td>0.912118</td>\n",
       "      <td>14954</td>\n",
       "      <td>0.693259</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>13176</td>\n",
       "      <td>458.342987</td>\n",
       "      <td>193.337387</td>\n",
       "      <td>87.448395</td>\n",
       "      <td>0.891861</td>\n",
       "      <td>13368</td>\n",
       "      <td>0.640669</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>14688</td>\n",
       "      <td>507.166992</td>\n",
       "      <td>211.743378</td>\n",
       "      <td>89.312454</td>\n",
       "      <td>0.906691</td>\n",
       "      <td>15262</td>\n",
       "      <td>0.646024</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3805</th>\n",
       "      <td>11441</td>\n",
       "      <td>415.858002</td>\n",
       "      <td>170.486771</td>\n",
       "      <td>85.756592</td>\n",
       "      <td>0.864280</td>\n",
       "      <td>11628</td>\n",
       "      <td>0.681012</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3806</th>\n",
       "      <td>11625</td>\n",
       "      <td>421.390015</td>\n",
       "      <td>167.714798</td>\n",
       "      <td>89.462570</td>\n",
       "      <td>0.845850</td>\n",
       "      <td>11904</td>\n",
       "      <td>0.694279</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3807</th>\n",
       "      <td>12437</td>\n",
       "      <td>442.498993</td>\n",
       "      <td>183.572922</td>\n",
       "      <td>86.801979</td>\n",
       "      <td>0.881144</td>\n",
       "      <td>12645</td>\n",
       "      <td>0.626739</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3808</th>\n",
       "      <td>9882</td>\n",
       "      <td>392.296997</td>\n",
       "      <td>161.193985</td>\n",
       "      <td>78.210480</td>\n",
       "      <td>0.874406</td>\n",
       "      <td>10097</td>\n",
       "      <td>0.659064</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3809</th>\n",
       "      <td>11434</td>\n",
       "      <td>404.709991</td>\n",
       "      <td>161.079269</td>\n",
       "      <td>90.868195</td>\n",
       "      <td>0.825692</td>\n",
       "      <td>11591</td>\n",
       "      <td>0.802949</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3810 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       Area   Perimeter  Major_Axis_Length  Minor_Axis_Length  Eccentricity  \\\n",
       "0     15231  525.578979         229.749878          85.093788      0.928882   \n",
       "1     14656  494.311005         206.020065          91.730972      0.895405   \n",
       "2     14634  501.122009         214.106781          87.768288      0.912118   \n",
       "3     13176  458.342987         193.337387          87.448395      0.891861   \n",
       "4     14688  507.166992         211.743378          89.312454      0.906691   \n",
       "...     ...         ...                ...                ...           ...   \n",
       "3805  11441  415.858002         170.486771          85.756592      0.864280   \n",
       "3806  11625  421.390015         167.714798          89.462570      0.845850   \n",
       "3807  12437  442.498993         183.572922          86.801979      0.881144   \n",
       "3808   9882  392.296997         161.193985          78.210480      0.874406   \n",
       "3809  11434  404.709991         161.079269          90.868195      0.825692   \n",
       "\n",
       "      Convex_Area    Extent  \n",
       "0           15617  0.572896  \n",
       "1           15072  0.615436  \n",
       "2           14954  0.693259  \n",
       "3           13368  0.640669  \n",
       "4           15262  0.646024  \n",
       "...           ...       ...  \n",
       "3805        11628  0.681012  \n",
       "3806        11904  0.694279  \n",
       "3807        12645  0.626739  \n",
       "3808        10097  0.659064  \n",
       "3809        11591  0.802949  \n",
       "\n",
       "[3810 rows x 7 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "64c417f5-9240-474c-9eb9-ee0d2e3af653",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0         Cammeo\n",
       "1         Cammeo\n",
       "2         Cammeo\n",
       "3         Cammeo\n",
       "4         Cammeo\n",
       "          ...   \n",
       "3805    Osmancik\n",
       "3806    Osmancik\n",
       "3807    Osmancik\n",
       "3808    Osmancik\n",
       "3809    Osmancik\n",
       "Name: Class, Length: 3810, dtype: object"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "244eb6cc-6930-4eb6-8e76-ddd3524f749f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Class\n",
       "Osmancik    2180\n",
       "Cammeo      1630\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "59196064-29bf-4c56-a931-f3c8dfbe6cda",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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YdEyvH8DERGRuXo9R+fq1atISkrC+PHjq8xLSEiAh4cHOnXqhPj4eNy4cUOZd/DgQej1eiXkAEBISAj0ej1SU1OVmoCAACXkAEBERARMJhPS0tKqbY/JZEJBQYHZg4iIiNSrXi8v//jjj+Hs7IyhQ4eaTR89ejRatWoFg8GAjIwMzJgxA//5z3+QkpICAMjOzoanp2eV9Xl6eiI7O1up8fLyMpvv6uoKrVar1Nxp/vz5mD17dl3sWrXu994NAO/fQEREVB/qNeisXr0ao0ePrvIFHBcXp/wcEBCAtm3bonv37jh27Bi6desGANWea1L5/0cq1abmdjNmzMC0adOU5wUFBfD19bVsp+6iLu7dAPD+DURERHWl3g5dffPNN8jMzMQf/vCHe9Z269YN9vb2OH36NIBb5/lcvXq1Sl1ubq4yimMwGKqM3OTl5aG0tLTKSE8lnU4HFxcXswcRERGpV70FnVWrViEoKAhdunS5Z+2JEydQWloKb29vAEBoaCiMRiOOHDmi1Bw+fBhGoxFhYWFKTUZGhtlVXjt27IBOp0NQUFAd7w0RERE1RhYfuiosLMSZM2eU5+fOnUN6ejrc3NzQokULALcOCf3rX//C4sWLqyx/9uxZJCQk4IUXXoCHhwdOnjyJ6dOno2vXrujRowcAoEOHDujfvz/i4uKwYsUKALcuLx84cCD8/f0BAOHh4ejYsSNiY2OxcOFCXL9+HfHx8YiLi+NIDREREQG4jxGd7777Dl27dkXXrl0BANOmTUPXrl3x1ltvKTWJiYkQEYwaNarK8lqtFrt27UJERAT8/f0xZcoUhIeHY+fOnbC1tVXqEhISEBgYiPDwcISHh6Nz58749NNPlfm2trZISkqCg4MDevTogREjRmDw4MFYtGiRpbtEREREKqWRO/9t9iOkoKAAer0eRqPR6qNARUVFyj14eD8cIqKHj5/DjYcl39/8X1dERESkWgw6REREpFoMOkRERKRaDDpERESkWgw6REREpFoMOkRERKRaDDpERESkWgw6REREpFoMOkRERKRaDDpERESkWgw6REREpFoMOkRERKRaDDpERESkWgw6REREpFoMOkRERKRaDDpERESkWgw6REREpFoMOkRERKRaDDpERESkWgw6REREpFoMOkRERKRaDDpERESkWgw6REREpFoMOkRERKRaDDpERESkWgw6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iIiISLUYdIiIiEi1GHSIiIhIter1v5cTERE9qHIRoKL+tyMiqPi/W8HZaKr/x9F1qfwe952jusGgQ0REDdreX361dhOoEeOhKyIiIlItjugQEVGD4+DggO3btz/UbRYXF2PQoEEAgC1btsDBweGhbfthbutRw6BzLxVlD2c7Iv/dlo0dUM/Hhh/afhER3QeNRgNHR0erbd/BwcGq26e6w6BzD07HEqzdBCIiIrpPPEeHiIiIVIsjOtXgsWEiIiJ1YNCpBo8NExERqQMPXREREZFqMegQERGRajHoEBERkWox6BAREZFqMegQERGRajHoEBERkWox6BAREZFqMegQERGRajHoEBERkWox6BAREZFqMegQERGRajHoEBERkWox6BAREZFqMegQERGRajHoEBERkWox6BAREZFqMegQERGRalkcdPbv34+oqCj4+PhAo9Fg8+bNZvNFBLNmzYKPjw8cHR3Ru3dvnDhxwqzGZDJh8uTJ8PDwgJOTE6Kjo3H58mWzmry8PMTGxkKv10Ov1yM2Nhb5+flmNRcvXkRUVBScnJzg4eGBKVOmoKSkxNJdIiIiIpWyOOjcvHkTXbp0wdKlS6ud/+677+K9997D0qVLcfToURgMBvTr1w83btxQaqZOnYpNmzYhMTERBw4cQGFhIQYOHIjy8nKlJiYmBunp6UhOTkZycjLS09MRGxurzC8vL8eAAQNw8+ZNHDhwAImJidiwYQOmT59u6S4RERGRWskDACCbNm1SnldUVIjBYJAFCxYo04qLi0Wv18uHH34oIiL5+flib28viYmJSs0vv/wiNjY2kpycLCIiJ0+eFABy6NAhpebgwYMCQH788UcREdm2bZvY2NjIL7/8otR89tlnotPpxGg01qr9RqNRANS6vj799ttv8uyzz8qzzz4rv/32m7WbQ0T0yOHncONhyfd3nZ6jc+7cOWRnZyM8PFyZptPp0KtXL6SmpgIA0tLSUFpaalbj4+ODgIAApebgwYPQ6/UIDg5WakJCQqDX681qAgIC4OPjo9RERETAZDIhLS2t2vaZTCYUFBSYPYiIiEi96jToZGdnAwC8vLzMpnt5eSnzsrOzodVq4erqetcaT0/PKuv39PQ0q7lzO66urtBqtUrNnebPn6+c86PX6+Hr63sfe0lERESNRb1cdaXRaMyei0iVaXe6s6a6+vupud2M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QosWLZCTk4O3334bBQUFGDNmDDQaDaZOnYp58+ahbdu2aNu2LebNm4cmTZogJiYGAKDX6zF+/HhMnz4d7u7ucHNzQ3x8vHIoDAA6dOiA/v37Iy4uDitWrAAATJgwAQMHDoS/v39d7xIRERE1UnUedC5fvoxRo0bh119/RfPmzRESEoJDhw7Bz88PAPCXv/wFRUVFmDhxIvLy8hAcHIwdO3bA2dlZWceSJUtgZ2eHESNGoKioCH379sXatWtha2ur1CQkJGDKlCnK1VnR0dFYunRpXe8OERERNWIaERFrN8JaCgoKoNfrYTQaeb4OERFRI2HJ9zf/1xURERGpFoMOERERqRaDDhEREakWgw4RERGpFoMOERERqRaDDhEREakWgw4RERGpFoMOERERqRaDDhEREakWgw4RERGpFoMOERERqRaDDhEREakWgw4RERGpFoMOERERqRaDDhEREakWgw4RERGpFoMOERERqRaDDhEREakWgw4RERGpFoMOERERqRaDDhEREakWgw4RERGpFoMOERERqRaDDhEREakWgw4RERGpFoMOERERqRaDDhEREakWgw4RERGpFoMOERERqRaDDhEREakWgw4RERGpFoMOERERqRaDDhEREalWnQed+fPn46mnnoKzszM8PT0xePBgZGZmmtWMHTsWGo3G7BESEmJWYzKZMHnyZHh4eMDJyQnR0dG4fPmyWU1eXh5iY2Oh1+uh1+sRGxuL/Pz8ut4lIiIiaqTqPOjs27cPkyZNwqFDh5CSkoKysjKEh4fj5s2bZnX9+/dHVlaW8ti2bZvZ/KlTp2LTpk1ITEzEgQMHUFhYiIEDB6K8vFypiYmJQXp6OpKTk5GcnIz09HTExsbW9S4RERFRI6UREanPDeTm5sLT0xP79u1Dz549Adwa0cnPz8fmzZurXcZoNKJ58+b49NNPMXLkSADAlStX4Ovri23btiEiIgKnTp1Cx44dcejQIQQHBwMADh06hNDQUPz444/w9/e/Z9sKCgqg1+thNBrh4uJSNztMRERE9cqS7+96P0fHaDQCANzc3Mym7927F56enmjXrh3i4uKQk5OjzEtLS0NpaSnCw8OVaT4+PggICEBqaioA4ODBg9Dr9UrIAYCQkBDo9Xql5k4mkwkFBQVmDyIiIlKveg06IoJp06bhmWeeQUBAgDI9MjISCQkJ2L17NxYvXoyjR4/iueeeg8lkAgBkZ2dDq9XC1dXVbH1eXl7Izs5Wajw9Pats09PTU6m50/z585XzefR6PXx9fetqV4mIiKgBsqvPlb/yyiv44YcfcODAAbPplYejACAgIADdu3eHn58fkpKSMHTo0BrXJyLQaDTK89t/rqnmdjNmzMC0adOU5wUFBQw7REREKlZvIzqTJ0/Gl19+iT179uDxxx+/a623tzf8/Pxw+vRpAIDBYEBJSQny8vLM6nJycuDl5aXUXL16tcq6cnNzlZo76XQ6uLi4mD2IiIhIveo86IgIXnnlFWzcuBG7d+9Gq1at7rnMtWvXcOnSJXh7ewMAgoKCYG9vj5SUFKUmKysLGRkZCAsLAwCEhobCaDTiyJEjSs3hw4dhNBqVGiIiInq01flVVxMnTsT69euxZcsWsyuf9Ho9HB0dUVhYiFmzZmHYsGHw9vbG+fPn8cYbb+DixYs4deoUnJ2dAQAvv/wytm7dirVr18LNzQ3x8fG4du0a0tLSYGtrC+DWuT5XrlzBihUrAAATJkyAn58fvvrqq1q1lVddERERNT6WfH/XedCp6fyYNWvWYOzYsSgqKsLgwYPx/fffIz8/H97e3ujTpw/mzJljdr5McXExXnvtNaxfvx5FRUXo27cvli1bZlZz/fp1TJkyBV9++SUAIDo6GkuXLkWzZs1q1VYGHSIiosbHqkGnMWHQISIianwa1H10iIiIiKyFQYeIiIhUi0GHiIiIVItBh4iIiFSLQYeIiIhUi0GHiIiIVItBh4iIiFSLQYeIiIhUi0GHiIiIVItBh4iIiFSLQYeIiIhUi0GHiIiIVItBh4iIiFSLQYeIiIhUi0GHiIiIVItBh4iIiFSLQYeIiIhUi0GHiIiIVItBh4iIiFSLQYeIiIhUi0GHiIiIVItBh4iIiFSLQYeIiIhUi0GHiIiIVItBh4iIiFSLQYeIiIhUy87aDaBHg4iguLj4vpYzmUwAAJ1OB41Gc1/bd3BwuO9liYio8WLQIYtUBhZLQ0txcTFGjhxZT626t88//xwODg4WLePg4MCARETUyDHokEWKi4sRERFh7WZY7H5D1vbt2+Ho6FjHrSEiooeF5+gQERGRanFEh4hUadiwYcjNzUXz5s2xYcMGazeHiKyEQYcs4uDggO3bt1u8XHFxMQYNGlQPLaqdLVu2WHyODoD7WsZS1jxRW63nIGVkZCA3NxcAkJubi4yMDAQEBFi5VURkDRoREWs3wloKCgqg1+thNBrh4uJi7eao2qN01VVeXp5F9dY8Uft+TtIGAFdX13poTd3p2bNnlWn79++3Qksaptv7h/1CjZEl39+NfkRn2bJlWLhwIbKystCpUye8//77ePbZZ63dLLqDRqO575N6mzRpUsetqV/WHLmy1P0GrIb85fjOO+/UOP31119/yK1peBYuXFjl+WuvvWal1hDVv0YddD7//HNMnToVy5YtQ48ePbBixQpERkbi5MmTaNGihbWbR0R3sHS0q6KiAgUFBbWuLykpQVJSUrXzkpKSMHjwYGi12lqty8XFBTY2ll2v0dBHugDgq6++qvKcQYfUrFEfugoODka3bt2wfPlyZVqHDh0wePBgzJ8//57L89AV1QceuqpZdYeU1ORBRrrqOwQCwEsvvYTy8vIq021tbbF69epar0etIbCxeRivmbpUl6+bR+LQVUlJCdLS0vDXv/7VbHp4eDhSU1OrXcZkMinnewCw6i+c1MvSD3QRua8TvHkysrpY85BneXk5xowZU6/baMiHOxurxnSY/H7Vxeum0QadX3/9FeXl5fDy8jKb7uXlhezs7GqXmT9/PmbPnv0wmkdUa4/S+UtbtmyxqN7Sv0APHTpkNsJ7p5dffhkhISG1Wtf9/PVJRA1Pow06le78a1REavwLdcaMGZg2bZryvKCgAL6+vvXaPiL6r/s5fOHu7l7r2latWt016IwaNcri7T8s9R0Cf/31V0yfPr3G+YsXL4aHh0et1sUQ2DDU92umrlnrddNog46HhwdsbW2rjN7k5ORUGeWppNPpoNPpHkbziMhK9u/f3ygvL38YIdDe3h6lpaVV5tnb2+Opp56yePtkXfX9mlGLRhvJtVotgoKCkJKSYjY9JSUFYWFhVmoVETUEd55g/TBu/NgY7Nq1y6LpRGrQaIMOAEybNg3//Oc/sXr1apw6dQqvvvoqLl68iD/96U/WbhoRWdGOHTvu+vxRFhUVddfnRGrTqC8vB27dMPDdd99FVlYWAgICsGTJklpfwsrLy4noUcQ7I1NjZ8n3d6MPOg+CQYeIiKjxseT7u1EfuiIiIiK6GwYdIiIiUi0GHSIiIlItBh0iIiJSLQYdIiIiUi0GHSIiIlItBh0iIiJSLQYdIiIiUi0GHSIiIlKtRvvfy+tC5U2hrflv64mIiMgyld/btfnnDo900Llx4wYAwNfX18otISIiIkvduHEDer3+rjWP9P+6qqiowJUrV+Ds7AyNRmPt5qCgoAC+vr64dOkS//fWbdgvNWPf1Ix9UzP2Tc3YNzVrSH0jIrhx4wZ8fHxgY3P3s3Ae6REdGxsbPP7449ZuRhUuLi5WfxE1ROyXmrFvasa+qRn7pmbsm5o1lL6510hOJZ6MTERERKrFoENERESqxaDTgOh0OsycORM6nc7aTWlQ2C81Y9/UjH1TM/ZNzdg3NWusffNIn4xMRERE6sYRHSIiIlItBh0iIiJSLQYdIiIiUi0GHbKaWbNm4cknn7R2M6ql0WiwefNmazfjns6fPw+NRoP09PQ6WV/v3r0xderUOllXXbqf30dd901D9bBeq3v37oVGo0F+fn6t6hvqa4kePQw69Sg1NRW2trbo37+/tZvywMaOHQuNRgONRgN7e3u0bt0a8fHxuHnz5n2vMz4+Hrt27arT9v3pT3+qMq99+/bQaDQYO3ZsrdeXlZWFyMjIOmnbvaxfvx62trbVtv1efH19kZWVhYCAgBpr7tY3EydOVPpGo9Fg/PjxmDNnjsXtqCt3ht/Kvrkftemb2rrfMHH7++b2x/18JtTHHwaWrDMsLAxZWVm1vknbxo0bzV5Lvr6+ePbZZ9G6dWvodDr4+voiKiqqzj4DGpJ58+bB1tYWCxYssFobHvS1V59B9WH/IcmgU49Wr16NyZMn48CBA7h48WKNdSKCsrKyh9iy+9O/f39kZWXh559/xttvv41ly5YhPj7e4vVU7m/Tpk3h7u5eZ+3z9fVFYmIiioqKlGnFxcU4d+4cHB0dLVqXwWCocgllSUlJrZe3pHb16tX4y1/+gsTERPz222+1Xg4AbG1tYTAYYGd395uc19Q3n332GVq0aKFMc3Z2hrOzs0VtsNT99A0AmEwmi7ZT276pb5Xvm9sfn332mVXbZKnS0lJotVoYDIZa/7scNzc35bV0/vx5ZGVl4fTp03j33Xdx/PhxJCcno0+fPpg0aVJ9Nt0q1qxZg7/85S9YvXr1PWtLS0vrrR1qeO3VCaF6UVhYKM7OzvLjjz/KyJEjZfbs2cq8PXv2CABJTk6WoKAgsbe3l927d0tFRYW888470qpVK3FwcJDOnTvLv/71L2W5srIyeemll6Rly5bi4OAg7dq1k/fff/+h7M+YMWNk0KBBZtP+8Ic/iMFguGe7a9rfmTNnSpcuXapsY+7cueLp6Sl6vV5mzZolpaWlEh8fL66urvLYY4/JqlWrzNpx+fJladmypdjZ2Ymtra1069ZNzp07JyIiQ4cOFQBmj3feeUd69OghLi4uotVqxc7OTvR6vURHRyvLAZA+ffrIoEGDZN68eeLh4SE6nU4cHBzEzc1N4uLi5MaNG1XaPm/ePPH29hY/P79a9eu5c+fE0dFR8vPzJTg4WD7++GOz+ePGjZPAwEApLi4WEZGSkhLp1q2bxMTEKMsDkO+//15ERK5fvy4xMTHi4eEhDg4O0qZNG+nRo4cMGjRIAgMDZd26dcq6ExISJDAwUAYNGiRjxowRANKpUyf585//rNT4+fnJ3LlzZdy4caLT6cTOzk7s7OzE399f/vGPf4iIyA8//CChoaECQJo2bSre3t7K6yA1NdWsb/R6vdja2oqjo6MMHjxYFi9eLHq9XkRE1qxZU+V3pdVqJT8/XwDIuHHjZPDgweLo6Cht2rSRvn37PnDfrF69ula/JwCyadOmGuevXr1a2rdvLzqdzqxvxowZI/369RMAsmHDBundu7c4OjoqfZOXlydxcXHi6emp9K1Wq1X6xsnJSXr27ClarbZK36xevVreeecdASD29vbK67lNmzayZcsW5X23c+dOCQoKEkdHRwkNDZUff/yxxv5es2aNsr/Lly+X6OhoadKkibz11lvK+vLy8pT9PnDggPTs2VMcHR2lWbNmEh4eLtevXxcRkV69eimvJTc3tyrbqvyMXLt2rYiIXLhwQaKjo8XBwUEAyJAhQyQ7O1vZVuXnxSeffCJ+fn7i4uIiI0eOlIKCAhER+fDDD8XHx0fKy8vNfjdRUVHyP//zP8rzL7/8Urp16yY6nU5atWqlfMaIiMyePVu8vb3l119/NVv+2WefrbLemuzdu1cee+wxKSkpER8fH9m3b5/Z/Mr9WLVqlbRq1Uo0Go1UVFRIfn6+xMXFSfPmzcXZ2Vn69Okj6enpynJnzpyR6Oho8fT0FCcnJ+nevbukpKTU2I7qPrMr7dmzR+zt7WX//v3KtEWLFom7u7tcuXJF+Ty4/VH52XjixAmJjIwUJycn8fT0lN///veSm5urrKdXr14yefJkee2118TV1VW8vLxk5syZynw/Pz+z9db2s/JBMOjUk1WrVkn37t1FROSrr76Sli1bSkVFhYj894u/c+fOsmPHDjlz5oz8+uuv8sYbb0j79u0lOTlZzp49K2vWrBGdTid79+4VkVsf5G+99ZYcOXJEfv75Z1m3bp00adJEPv/883rfn+reNJMnTxZ3d/d7trum/a0u6Dg7O8ukSZPkxx9/lFWrVgkAiYiIkLlz58pPP/0kc+bMEXt7e7l48aKIiNy8eVPatm0rbdq0kT59+sjrr78uXl5e4u/vLyaTSXr37i1PPvmkeHp6yogRIyQrK0sSExNl/fr14ufnJ4MGDZJevXpJu3btZNSoUcpylUGnadOmMmrUKPH09JTnn39ejh8/Lrt27ZJWrVrJmDFjzNretGlTiY2NlYyMDDl+/Hit+vXNN9+U4cOHi4jIBx98ID179jSbf+PGDWndurVMnTpVRERef/11adGiheTn54tI1S/zSZMmyZNPPilHjx6Vc+fOSUpKijz33HMyaNAgee+996Rv377Kuvv27StLliy5Z9Bxc3OTmJgYad68uYwePVpsbGzk73//u7i5ucmKFSvEx8dH+vfvLwDE19dXvLy8ZMiQITJ8+HDx8/OT2NhYadq0qURERIhGo5Hp06dLZmam/OMf/xA3Nzcl6Pz2228yffp06dSpk2RlZcmrr74qQ4YMERFRQs/69evl9OnTMmXKFHFycpKWLVs+UN98+eWXtfo93S3ofPTRR+Lt7S0bNmyQn3/+WTZs2CBubm6ydu1as6DTvn172bp1q2RmZsrw4cOlRYsWEhwcLJ06dZIlS5aIRqORcePGyUcffST/+Mc/xMXFRQDIyy+/LIcOHZIxY8aIwWCQjIwMycrKktdee03at28vAMRgMMgf//hH0Wq1MnToUGnatKls2bJFAEhwcLDs3btXTpw4Ic8++6yEhYVV299ZWVny22+/Kfvr6ekpq1atkrNnz8r58+erBJ3vv/9edDqdvPzyy5Keni4ZGRnywQcfKF96lUHn2rVrotFoxMXFRf72t78p2xIRiYuLkxdeeEEqKiqka9eu8swzz0jv3r0lMjJSunXrJr169VL6eebMmdK0aVMZOnSoHD9+XPbv3y8Gg0HeeOMNERG5du2aaLVa2blzp7LM9evXRavVyvbt20VEJDk5WVxcXGTt2rVy9uxZ2bFjh7Rs2VJmzZolIrf+mAwNDZXBgweLiMjy5ctFr9fL+fPna/U6ERGJjY2V+Ph4ERGZPn26Wciq3A8nJyeJiIiQY8eOyX/+8x+pqKiQHj16SFRUlBw9elR++uknmT59uri7u8u1a9dERCQ9PV0+/PBD+eGHH+Snn36S//f//p84ODjIhQsXqm3H3YKOiMhrr70mfn5+kp+fL+np6aLT6WTjxo0iIpKfny+hoaESFxen/L7KysrkypUr4uHhITNmzJBTp07JsWPHpF+/ftKnTx9lvb169RIXFxeZNWuW/PTTT/Lxxx+LRqORHTt2iIhITk6OEqqzsrIkJyen1n17vxh06klYWJgy2lJaWioeHh5K+q78wNi8ebNSX1hYKA4ODpKammq2nvHjx8uoUaNq3M7EiRNl2LBh9bAH5u580xw+fFjc3d1l+PDh92x3dfsrItUGHT8/P7O/nPz9/eXZZ59VnpeVlYmTk5N89tlnInIrUPr7+yvty83NFZ1OJzqdTj755BNxcHCQkSNHisFgMAsmlctVVFQob7xjx46Jo6OjbN++XQk6Xl5esmzZMnF1dZXCwkJl+aSkJLGxsVH+4hwzZox4eXmJyWSqdZ+Wl5eLr6+v0i+5ublib28vp0+fNqtLTU0Ve3t7efPNN8XOzs7sL8Q7v8yjoqJk3LhxZsvf2Tfnzp2T8+fPi4ODg+Tm5t4z6Pz+978XX19fWb9+vVRUVIinp6csX75c5syZI61btxZXV1c5ceKEAJB//vOfSt/s27dPAMjgwYPFy8tLhg8fLgMGDDBr2+jRo5WgI/Lf18SdfQNAbGxslL4pLCwUjUYj77333gP1TW3dLehU9s3t5syZI6GhoTJmzBixtbUVAKLT6cTJyUmcnJzklVdeUfYpMzNTRo4cWaVv/Pz8xNbWtkrfVO5/5fsOgPzv//6viNx637344oui0WiU0Z7bv/iTkpIEgBQVFVVZ5537WxkgK90ZdEaNGiU9evSosc8qg87hw4cFgDRv3lyWLFliVnP48GGxtbWVzz77TGxtbSU9PV3s7e2VYAZAjhw5orS1SZMmygiOyK0v6+DgYOV5dHS0vPTSS8rzFStWiMFgkLKyMhERefbZZ2XevHlmbfj000/F29tbeX727FlxdnaW119/XZo0aWI2CnovRqNRmjRpoozEfP/999KkSRMxGo1KzcyZM8Xe3t7sC37Xrl3i4uKijE5WeuKJJ2TFihU1bq9jx47ywQcfVDuv8rVX+ZqrfPztb38TERGTySRdu3aVESNGSKdOneQPf/iD2fK3j8hVevPNNyU8PNxs2qVLlwSAZGZmKss988wzZjVPPfWUvP7668rze42Q1rVH+r+X15fMzEwcOXIEGzduBADY2dlh5MiRWL16NZ5//nmlrnv37srPJ0+eRHFxMfr162e2rpKSEnTt2lV5/uGHH+Kf//wnLly4gKKiIpSUlDy0K5e2bt2Kpk2boqysDKWlpRg0aBDi4+Px73//+57tBsz3tyadOnWCjc1/Tx3z8vIyO5nU1tYW7u7uyMnJAQCkpaXhzJkzOHv2LEQELVu2RFlZGcrLy5GYmIgBAwbAwcHBbBtnz57FggULcPr0abNthYaGoqSkBGfPnlWmBQYG4vTp0+jSpQucnJyU6T169EBFRQUyMzPh5eWl1Gq12nvuY6UdO3bg5s2byknPHh4eCA8Px+rVqzFv3jyzdsXHx2POnDl4/fXX0bNnzxrX+fLLL2PYsGE4duwYwsPDMXjwYGWeh4cHBgwYgI8//hgiggEDBsDDw+Oe7WzdujXWrVuH8ePHIy4uDkVFRZgyZQpsbGxgY2OD4OBgNGnSBADQuXNntGvXDhUVFbhx4waAW+cCBQYG4syZMxgyZIjZup9++mls3br1nn0DAE8++aTSN05OTnB2doa7u/sD9U1YWNg99/9ucnNzcenSJaVvKpWVlUGv16Ndu3YICQnBt99+i/Xr16Nz584AABsbGyxduhTNmzdHu3btkJmZWaVviouLazy/6M7Pi4ULF2LJkiXK+87Z2Rl5eXkAoGwTALy9vQEAOTk5ZudmVede79f09HS8+OKLd60Bbp2TV5Onn34anTp1QkJCAnx9fbF79260aNECPXv2hEajQbNmzXDq1Ck89dRTAICWLVuanUPm7e2tfBYAwOjRozFhwgQsW7YMOp0OCQkJ+N3vfqec0J6WloajR49i7ty5yjLl5eUoLi7Gb7/9hiZNmqB169ZYtGgR/vjHP2LkyJEYPXr0Pfex0vr169G6dWt06dIFwK3XbOvWrZGYmIgJEyYodX5+fmjevLnyPC0tDYWFhVXOWSwqKlI+j27evInZs2dj69atuHLlCsrKylBUVHTX8z/79OmD5cuXm01zc3MDAGi1Wqxbtw6dO3eGn58f3n///XvuX1paGvbs2YOmTZtWmXf27Fm0a9cOgPlrDqj6e3rYGHTqwapVq1BWVobHHntMmSYisLe3Vz58AJh9cVZUVAAAkpKSzJYDoJwU+8UXX+DVV1/F4sWLERoaCmdnZyxcuBCHDx+uz91RVL5p7O3t4ePjA3t7e2Xbd2t3pdv3tyb29vZmzyuv8rpzWmV/VVRUICgoCI899hhu3LiB5cuXY8+ePfjb3/6GjIwMLF++HF988YXZ8lFRUSgqKoK/vz/ef/99iAheeOEFLFmyBP369UPz5s0xceJEpc0iUuMJmLdPr83+3W716tW4fv26EhIq9+f777/HnDlzlA/niooKfPvtt7C1tcXp06fvus7IyEhcuHABSUlJ2LlzJ/r27YsnnngCbdq0AQC89NJLeOWVVwAA//jHP2rVzsov25UrVyI4OBhRUVHo168fpkyZgnnz5uH8+fNK7e2/q8q+ERE4OTkhNze3Sj/W9CVYXd98//33yM7OVvpGo9GgrKzsgfpm0qRJWLRoUa36oTqVr8PKvrmdra0tZs+erexD69atld/DnZdoV/cau/N1X912k5KS0Lt3b+W1C9x63wUGBip9W93vpHL5u7nX67m2J/i3bdsWGo2mxpNu//CHP2DOnDlo2rQp1qxZg3Hjxpm9dm7vl7t9FgC33tsVFRVISkrCU089hW+++QbvvfeeMr+iogKzZ8/G0KFDq7Tj9j+I9u/fD1tbW5w/fx5lZWW1PqF99erVOHHihFl9RUUFVq1aZRZ07uzbiooKeHt7Y+/evVXW2axZMwDAa6+9hu3bt2PRokVo06YNHB0dMXz48Lue3O/k5KS85qqTmpoKALh+/TquX79+z995RUUFoqKi8M4771SZVxmigXv/nh42XnVVx8rKyvDJJ59g8eLFSE9PVx7/+c9/4Ofnh4SEhGqX69ixI3Q6HS5evIg2bdqYPXx9fQEA33zzDcLCwjBx4kR07doVbdq0MRt9qG+Vbxo/Pz/lhVybdtenbt264fTp03B0dFTa99JLL6GiogJlZWWIiIiAVqtVPvSvXbuGU6dOYdSoUcjJyUFYWJjyF6K3tzfatGlT5fLZjh07Ij093exS+m+//RY2NjbKXzCWunbtGrZs2YLExESz10l6ejoKCwvx9ddfK7ULFy7EqVOnsG/fPmzfvh1r1qy567qbN2+OsWPHYt26dXj//feRmZmpzOvfvz9KSkpQUlKCiIiIWrXV2dkZjz32GH7++We0adMGOp0Obm5uaNOmDUJDQ5Genm52tVhl39z5Adu+fXscOXLEbNp3331n9lyr1cJkMlXpGwB47733qvTN119//UB989FHH9WqD2ri5eVl1je3P1q1anXP5XNzc/HTTz9V2zdardbsakytVovy8nIA5u874L+vXUvfd7ev01KdO3eu1aXhbm5uiIiIQGFhYbVXFUZFRSE/Px8XLlxARkYGxowZA+DWqJXRaESHDh1q3SZHR0cMHToUCQkJ+Oyzz9CuXTsEBQUp87t164bMzMwqv6s2bdooo7uff/45Nm7ciL179+LSpUu1vt3C8ePH8d1332Hv3r1m7+f9+/fj6NGjyMjIqHHZbt26ITs7G3Z2dlXaVTnq+s0332Ds2LEYMmQIAgMDYTAYzP7IsNTZs2fx6quvYuXKlQgJCcH//M//mIWR6l4b3bp1w4kTJ9CyZcsq7bTkDz17e/v7ft3dD47o1LGtW7ciLy8P48ePr/KFOXz4cKxatQpLliypspyzszPi4+Px6quvoqKiAs888wwKCgqQmpqKpk2bYsyYMWjTpg0++eQTbN++Ha1atcKnn36Ko0eP1uoDtb7Upt31afTo0Vi4cCF27dqFtm3b4ty5c7h48SKioqLw5z//Gba2tmjZsiUKCgpgNBpRXl4Od3d3XLp0CS4uLujZs6dy2XJGRgb27NmD1157rco2Zs6ciTFjxmDWrFnIzc3F5MmTERsbqxy2stSnn34Kd3d3vPjii2aHzwBg4MCBWLVqFQYOHIj09HS89dZb+Pe//40ePXrg73//O/785z+jV69eaN26dZX1vvXWWwgKCkKnTp1gMpmwdetW5S9C4NYow6lTp5Sf71RcXIzc3FwlXJSUlMBkMmHWrFmYMmUKXFxcYDKZcPXqVaxZswbXrl2Dg4MDpk+fDgA4evQoFixYgNjYWHh6epqte/LkyejZsyfee+89REVFYffu3fj666/N/mJv2bIlfv75Z7i4uKBPnz7Q6/XKyGDLli3N+qa8vBybN2/Gxo0b77tvLPkSPXfuXJWbD7Zp08asbyIjI2EymfDdd98po7eVf3H/+uuvyM7OBgAlNHfu3BnDhg3D+PHjMW3aNMTFxSEkJARlZWW4fv06ysvLMXHiRPzpT3+CVqvFTz/9hD179iAwMBBTp07Fq6++CuDWfZ++//575X1XWy1btlT26/HHH4ezs3Ot/zP1jBkzEBgYaNa+PXv24MUXX6xySHTZsmVo3749FixYAA8PD3Tp0gUuLi5ISUnB8uXLMXz4cCQmJqJZs2bIycnBlStXMHHiRPTq1atWh7xvN3r0aERFReHEiRP4/e9/bzbvrbfewsCBA+Hr66u893744QccP34cb7/9Ni5fvoyXX34Z77zzDp555hmsXbsWAwYMQGRkJEJCQu663VWrVuHpp5+u9vBpaGhojZ/9APD8888jNDQUgwcPxjvvvAN/f39cuXIF27Ztw+DBg9G9e3e0adMGGzduRFRUFDQaDd588817jpKYTCblNVfJzs4Orq6uiI2NRXh4OMaNG4fIyEgEBgZi8eLFyudfy5YtcfjwYZw/fx5NmzaFm5sbJk2ahJUrV2LUqFF47bXX4OHhgTNnziAxMRErV66s9T2vWrZsiV27dqFHjx7Q6XRwdXWt1XL37aGdDfSIGDhwoLzwwgvVzktLSxMAsnjx4iqXaYqIVFRUyN///nfx9/cXe3t7ad68uURERCgnWBYXF8vYsWNFr9dLs2bN5OWXX5a//vWv1Z5MWNfudgb/vdpd3WWpItWfjHznNqo7Ic7Pz8/spMasrCx54oknRKvVik6nk9atW0tcXJxyAmBOTo40b95c7OzsBIAsWrRIOnToIDqdTlxdXUWv1wsA8fLyUpbDbZeXi9y6hLpPnz73vLy8tgIDA2XixInVztuwYYPY2dnJ+fPnpWPHjjJhwgSz+UOGDJGwsDApKyurcsLtnDlzpEOHDuLo6Chubm4yaNAgGTZs2F3bdvvJyNU9Jk2aJCK3Lkd/8sknRaPRiIODg/Ts2VM2btxodnm5Xq9X+iYvL0+5aq5y+x999JE89thjyuXlb7/9thgMBqUtxcXFymXSuONy502bNpn1jY2NjdlVOffTNz///HOtfl819c2ePXvM+kar1Yqrq6vSNzX1a9u2bQWAbNmyRcaNGyfu7u5ib29vdnn522+/LW5ubhIWFiY6nU6aNWsmXl5eytVYq1evlr///e8CQOzs7Mzed3q9Xl5//fUq77vvv//e7FLh4uJiGTZsmDRr1qza/r5dde/jvXv3mrUvIiJCmX/ne/err74Sd3d3pQ8ee+wxiY6Olj179siuXbsEgHTv3l2cnJzE2dlZXnzxxWovL7/dkiVLqlyeXFZWJt7e3gJAzp49W+V3mZycLGFhYeLo6CguLi7y9NNPy0cffSQVFRXSt29fiYiIUK6QFRF59dVX5YknnjB7v9/JZDKJu7u7vPvuu9XOX7x4sXh4eIjJZKrxBPCCggKZPHmy+Pj4iL29vfj6+sro0aOVK0zPnTsnffr0EUdHR/H19ZWlS5dW+/lYqabXnr+/f7WX0W/evFm0Wq3yfsnMzJSQkBBxdHQ0e8389NNPMmTIEGnWrJk4OjpK+/btZerUqUqfVdemys+YSl9++aW0adNG7OzsHsrl5RqRu5wpRvQIMplMcHBwQEpKitnJ41T34uLi8OOPP+Kbb76xdlManEepbxISEvDnP/8ZV65cseiEfqLa4KErotsUFBRg48aNsLGxQfv27a3dHNVZtGgR+vXrBycnJ3z99df4+OOPsWzZMms3q0F4FPvmt99+w7lz5zB//nz88Y9/ZMih+lHvY0ZEjcjUqVPF09NTFi5c+EDr2b9/f5X7V9z+eNjmzp1bY1v69+//0Nrx4osvKocKNRqN2b1l2DcvSvPmzcXBwUE6duwoy5cvf2jbtpaZM2eKnZ2dPPfcc3c9NNQQrFu3rsbXSceOHa3dPLoLHroiqgdFRUX45Zdfapx/t0s+60Pl5aPVcXR0rHJrgPrEvqHG6MaNG7h69Wq18+zt7eHn5/eQW0S1xaBDREREqsX76BAREZFqMegQERGRajHoEBERkWox6BAREZFqMegQERGRajHoEBERkWox6BAREZFqMegQERGRav1/2tb9wsaFAZkAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b3a1eff8-2dd2-481a-8f71-e394c68d1469",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import MinMaxScaler\n",
    "scaler=MinMaxScaler()\n",
    "x_scaled=scaler.fit_transform(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "45cb7240-cdcf-4b7f-b8db-4001d66ed2df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.67593733, 0.87923163, 0.90121587, ..., 0.88801055, 0.69391702,\n",
       "        0.20757716],\n",
       "       [0.62533005, 0.71409491, 0.64808716, ..., 0.69197988, 0.64600914,\n",
       "        0.32456423],\n",
       "       [0.62339377, 0.75006612, 0.73434911, ..., 0.78984635, 0.63563643,\n",
       "        0.53857594],\n",
       "       ...,\n",
       "       [0.43002992, 0.44045819, 0.40864083, ..., 0.60847407, 0.43266526,\n",
       "        0.35564534],\n",
       "       [0.20515754, 0.17532451, 0.16992207, ..., 0.56901705, 0.20868495,\n",
       "        0.44453926],\n",
       "       [0.34175321, 0.24088172, 0.16869838, ..., 0.28376388, 0.34001406,\n",
       "        0.84022485]])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_scaled"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "2e009388-2c43-43eb-81a3-404c79d3178c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "x_train,x_test,y_train,y_test=train_test_split(x_scaled,y,random_state=0,test_size=0.2,stratify=y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c7c24ab5-7f5b-4973-9f46-4321b456380e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((3048, 7), (762, 7), (3048,), (762,))"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train.shape,x_test.shape,y_train.shape,y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "e6bc73f8-fb7f-4c7a-af45-ebe0c2e63a12",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-4 {color: black;background-color: white;}#sk-container-id-4 pre{padding: 0;}#sk-container-id-4 div.sk-toggleable {background-color: white;}#sk-container-id-4 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-4 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-4 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-4 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-4 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-4 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-4 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-4 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-4 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-4 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-4 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-4 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-4 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-4 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-4 div.sk-item {position: relative;z-index: 1;}#sk-container-id-4 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-4 div.sk-item::before, #sk-container-id-4 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-4 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-4 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-4 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-4 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-4 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-4 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-4 div.sk-label-container {text-align: center;}#sk-container-id-4 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-4 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-4\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>KNeighborsClassifier(n_neighbors=50)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-4\" type=\"checkbox\" checked><label for=\"sk-estimator-id-4\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">KNeighborsClassifier</label><div class=\"sk-toggleable__content\"><pre>KNeighborsClassifier(n_neighbors=50)</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "KNeighborsClassifier(n_neighbors=50)"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "knn=KNeighborsClassifier(n_neighbors=50)\n",
    "knn.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "386a97ad-e654-401f-bdb3-31dfb30c4370",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred=knn.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "802420dd-7269-4ff9-a498-e32ca112d5d8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9304461942257218"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_pred,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "19338c6d-888e-4f5c-8ae1-adc8a246f1fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "error=[]\n",
    "for i in range(1,150):\n",
    "    knn=KNeighborsClassifier(n_neighbors=i)\n",
    "    knn.fit(x_train,y_train)\n",
    "    y_pred=knn.predict(x_test)\n",
    "    error.append(np.mean(y_pred!=y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "1d6cc823-72e4-41ce-b479-c8dc7f177c7c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0.12860892388451445,\n",
       " 0.12073490813648294,\n",
       " 0.09055118110236221,\n",
       " 0.09580052493438321,\n",
       " 0.08530183727034121,\n",
       " 0.08792650918635171,\n",
       " 0.08923884514435695,\n",
       " 0.08530183727034121,\n",
       " 0.08267716535433071,\n",
       " 0.08005249343832022,\n",
       " 0.07480314960629922,\n",
       " 0.07742782152230972,\n",
       " 0.07480314960629922,\n",
       " 0.07086614173228346,\n",
       " 0.07086614173228346,\n",
       " 0.07349081364829396,\n",
       " 0.07480314960629922,\n",
       " 0.07611548556430446,\n",
       " 0.07742782152230972,\n",
       " 0.06955380577427822,\n",
       " 0.06824146981627296,\n",
       " 0.07086614173228346,\n",
       " 0.06692913385826772,\n",
       " 0.06955380577427822,\n",
       " 0.06955380577427822,\n",
       " 0.06955380577427822,\n",
       " 0.06955380577427822,\n",
       " 0.07217847769028872,\n",
       " 0.07349081364829396,\n",
       " 0.07217847769028872,\n",
       " 0.07086614173228346,\n",
       " 0.06955380577427822,\n",
       " 0.06955380577427822,\n",
       " 0.06955380577427822,\n",
       " 0.06955380577427822,\n",
       " 0.06824146981627296,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07480314960629922,\n",
       " 0.07349081364829396,\n",
       " 0.06955380577427822,\n",
       " 0.06692913385826772,\n",
       " 0.06824146981627296,\n",
       " 0.06955380577427822,\n",
       " 0.07086614173228346,\n",
       " 0.06561679790026247,\n",
       " 0.07086614173228346,\n",
       " 0.06824146981627296,\n",
       " 0.06955380577427822,\n",
       " 0.07086614173228346,\n",
       " 0.07217847769028872,\n",
       " 0.07217847769028872,\n",
       " 0.07217847769028872,\n",
       " 0.06955380577427822,\n",
       " 0.07217847769028872,\n",
       " 0.07086614173228346,\n",
       " 0.07217847769028872,\n",
       " 0.07217847769028872,\n",
       " 0.07217847769028872,\n",
       " 0.06955380577427822,\n",
       " 0.07086614173228346,\n",
       " 0.07217847769028872,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07217847769028872,\n",
       " 0.07217847769028872,\n",
       " 0.07349081364829396,\n",
       " 0.06955380577427822,\n",
       " 0.07086614173228346,\n",
       " 0.06955380577427822,\n",
       " 0.07349081364829396,\n",
       " 0.07217847769028872,\n",
       " 0.07217847769028872,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07217847769028872,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07217847769028872,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07217847769028872,\n",
       " 0.07217847769028872,\n",
       " 0.07349081364829396,\n",
       " 0.07480314960629922,\n",
       " 0.07349081364829396,\n",
       " 0.07480314960629922,\n",
       " 0.07480314960629922,\n",
       " 0.07480314960629922,\n",
       " 0.07480314960629922,\n",
       " 0.07480314960629922,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07217847769028872,\n",
       " 0.07217847769028872,\n",
       " 0.07217847769028872,\n",
       " 0.07217847769028872,\n",
       " 0.07217847769028872,\n",
       " 0.07217847769028872,\n",
       " 0.07086614173228346,\n",
       " 0.07349081364829396,\n",
       " 0.07086614173228346,\n",
       " 0.07217847769028872,\n",
       " 0.07217847769028872,\n",
       " 0.07349081364829396,\n",
       " 0.07086614173228346,\n",
       " 0.07480314960629922,\n",
       " 0.06955380577427822,\n",
       " 0.07480314960629922,\n",
       " 0.07349081364829396,\n",
       " 0.07611548556430446,\n",
       " 0.07480314960629922,\n",
       " 0.07480314960629922,\n",
       " 0.07480314960629922,\n",
       " 0.07480314960629922,\n",
       " 0.07480314960629922,\n",
       " 0.07611548556430446,\n",
       " 0.07611548556430446,\n",
       " 0.07611548556430446,\n",
       " 0.07611548556430446,\n",
       " 0.07742782152230972,\n",
       " 0.07611548556430446,\n",
       " 0.07480314960629922,\n",
       " 0.07349081364829396,\n",
       " 0.07480314960629922,\n",
       " 0.07480314960629922,\n",
       " 0.07480314960629922,\n",
       " 0.07611548556430446,\n",
       " 0.07611548556430446,\n",
       " 0.07611548556430446,\n",
       " 0.07611548556430446,\n",
       " 0.07480314960629922,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396,\n",
       " 0.07349081364829396]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "c04f77db-706e-4b74-80dc-44a9b5286960",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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a6t0z9///ndBr9cL27ZtE44ePSrccccdQnx8vGA0Gv04cu9y3iUkCMNvzgcOHBDUarXw5JNPCmfOnBHefvttISQkRHjrrbeke4bbnO+55x5h9OjRwscffywUFRUJ27ZtE2JiYoQ//vGP0j1Dfc5NTU1CQUGBUFBQIAAQnn32WaGgoEDaEePO/JYvXy4kJiYKn3/+uXD48GHhJz/5iTB16lTBYrH4a1p96mvOZrNZuOGGG4TExEShsLDQ5TXNZDJJzzGc5tyTrruEBGHozdldDFh68OKLLwopKSmCRqMRpk+fLm37HeoA9PixceNG6R6bzSY88cQTQlxcnKDVaoUf/ehHwtGjR/036EHQNWAZjnP+6KOPhPT0dEGr1QoTJkwQXn75ZZfPD7c5G41G4aGHHhKSk5MFnU4njBkzRli9erXLL66hPuevvvqqx3+/99xzjyAI7s2vra1NeOCBB4QRI0YIwcHBws9//nOhtLTUD7NxT19zLioq6vU17auvvpKeYzjNuSc9BSxDbc7uUgiCIPgik0NERETkKdawEBERUcBjwEJEREQBjwELERERBTwGLERERBTwGLAQERFRwGPAQkRERAGPAQsREREFPAYsREREFPAYsBAREVHAY8BCREREAY8BCxEREQU8BixEREQU8P5/heg3tWumXpcAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(range(1,150),error)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b105a99a-7b61-4d32-9889-512f66d91fc1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
