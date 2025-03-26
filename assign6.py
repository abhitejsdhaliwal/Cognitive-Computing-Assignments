{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Assignment 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
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
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "M = float(input(\"Enter a value : \"))\n",
    "x = np.linspace(-10,10,100)\n",
    "y1 = M * x**2\n",
    "y2 = M * np.sin(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      
      "text/plain": [
       "<Figure size 800x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8,6))\n",
    "plt.plot(x,y1,label = 'M*x^2',color = 'blue',linestyle = '-')\n",
    "plt.plot(x,y2,label = 'M*sin(x)',color = 'red',linestyle = '--')\n",
    "plt.legend()\n",
    "plt.grid(True)\n",
    "plt.title('Plot of y = M*x^2 and y = M*sin(x)')\n",
    "plt.xlabel('X ----->')\n",
    "plt.ylabel('Y ----->')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q2."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      
      "text/plain": [
       "<Figure size 800x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data = {\n",
    "    'Subjects' : ['Maths','Physics','Chemistry','English','PE'],\n",
    "    'Scores' : [95,94,97,91,98]\n",
    "}\n",
    "df = pd.DataFrame(data)\n",
    "plt.figure(figsize = (8,6))\n",
    "colors = sns.color_palette('husl',len(df))\n",
    "sns.barplot(x='Subjects',y='Scores',data=df,hue='Subjects',palette=colors,legend=False)\n",
    "\n",
    "for i,score in enumerate(df['Scores']):\n",
    "    plt.text(i,score+1,str(score),ha='center',fontsize=12)\n",
    "\n",
    "plt.grid(axis='y',linestyle='--',alpha=0.7)\n",
    "plt.title('Score Sheet of different Subjects')\n",
    "plt.xlabel('Subjects ---->')\n",
    "plt.ylabel('Scores ---->')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q3."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      
      "text/plain": [
       "<Figure size 1000x1000 with 4 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "Rno = 102317111\n",
    "np.random.seed(Rno)\n",
    "\n",
    "data = np.random.randn(50)\n",
    "\n",
    "fig,axes = plt.subplots(2,2,figsize=(10,10))\n",
    "\n",
    "axes[0,0].plot(np.cumsum(data),color='blue',linestyle='-',marker='o',markersize=4)\n",
    "axes[0,0].set_title('Cumulative Sum Plot')\n",
    "axes[0,0].set_xlabel('Index')\n",
    "axes[0,0].set_ylabel('Cumulative Sum')\n",
    "axes[0,0].grid(True)\n",
    "\n",
    "axes[0,1].scatter(range(50),data,color='red',alpha=0.7)\n",
    "axes[0,1].set_title('Scatter Plot with Random noise')\n",
    "axes[0,1].set_xlabel('Index')\n",
    "axes[0,1].set_ylabel('Value')\n",
    "axes[0,1].grid(True)\n",
    "\n",
    "axes[1,0].axis('off')\n",
    "axes[1,1].axis('off')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q4."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
     
      "text/plain": [
       "<Figure size 1000x800 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset = pd.read_csv('company_sales_data.csv')\n",
    "plt.figure(figsize=(10,8))\n",
    "sns.lineplot(data=dataset,x='month_number',y='total_profit',marker='o',color='blue')\n",
    "plt.title('Total Profit per Month')\n",
    "plt.xlabel('Month Number')\n",
    "plt.ylabel('Total Profit')\n",
    "plt.grid(True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      
      "text/plain": [
       "<Figure size 1200x800 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(12,8))\n",
    "product_cols = dataset.columns[1:7]\n",
    "for product in product_cols:\n",
    "    sns.lineplot(data=dataset,x='month_number',y=product,marker='o',label=product)\n",
    "\n",
    "plt.title('Product sales per Month')\n",
    "plt.xlabel('Month number')\n",
    "plt.ylabel('Sales units')\n",
    "plt.legend(title='Products')\n",
    "plt.grid(True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\eshaa\\AppData\\Local\\Temp\\ipykernel_26300\\3791039285.py:3: FutureWarning: \n",
      "\n",
      "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
      "\n",
      "  sns.barplot(x=data_sum.index,y=data_sum.values,palette='viridis')\n"
     ]
    },
    {
     "data": {
      
      "text/plain": [
       "<Figure size 1400x700 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data_sum = dataset.sum()\n",
    "plt.figure(figsize=(14,7))\n",
    "sns.barplot(x=data_sum.index,y=data_sum.values,palette='viridis')\n",
    "plt.title('Total Sum of each attribute')\n",
    "plt.xlabel('Attributes')\n",
    "plt.ylabel('Total Sum')\n",
    "plt.xticks(rotation=30)\n",
    "plt.grid(axis='y',linestyle='--',alpha=0.7)\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}