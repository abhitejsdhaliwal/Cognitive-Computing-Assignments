{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 4  1  9]\n",
      " [12  3  1]\n",
      " [ 4  5  6]]\n",
      "Sum of all elements: 45\n",
      "Sum of elements row-wise:\n",
      " [[14]\n",
      " [16]\n",
      " [15]]\n",
      "Sum of elements column-wise: [[20  9 16]]\n"
     ]
    }
   ],
   "source": [
    "gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')\n",
    "print(gfg)\n",
    "\n",
    "sum = np.sum(gfg)\n",
    "print(\"Sum of all elements:\",sum)\n",
    "\n",
    "row_wise_sum = np.sum(gfg, axis=1)\n",
    "print(\"Sum of elements row-wise:\\n\", row_wise_sum)\n",
    "\n",
    "column_wise_sum = np.sum(gfg, axis=0)\n",
    "print(\"Sum of elements column-wise:\", column_wise_sum)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sorted array: [ 10  16  16  52  54  62 453]\n",
      "Indices of sorted array: [0 3 4 1 5 2 6]\n",
      "4 smallest elements: [10 16 16 52]\n",
      "5 largest elements: [ 16  52  54  62 453]\n",
      "Integer elements: [1. 2. 3. 2.]\n",
      "Float elements: [1.  1.2 2.2 2.  3.  2. ]\n",
      "Float elements: [1.2 2.2]\n"
     ]
    }
   ],
   "source": [
    "array = np.array([10, 52, 62, 16, 16, 54, 453])\n",
    "sorted_array = np.sort(array)\n",
    "print(\"Sorted array:\", sorted_array)\n",
    "\n",
    "indices = np.argsort(array)\n",
    "print(\"Indices of sorted array:\", indices)\n",
    "\n",
    "smallest_4 = np.sort(array)[:4]\n",
    "print(\"4 smallest elements:\", smallest_4)\n",
    "\n",
    "largest_5 = np.sort(array)[-5:]\n",
    "print(\"5 largest elements:\", largest_5)\n",
    "\n",
    "array2= np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])\n",
    "\n",
    "integer_elements = array2[array2 == array2.astype(int)]\n",
    "print(\"Integer elements:\", integer_elements)\n",
    "\n",
    "float_elements = array2[array2 == array2.astype(float)]\n",
    "print(\"Float elements:\", float_elements)\n",
    "\n",
    "float_elements = array2[array2 != array2.astype(int)]\n",
    "print(\"Float elements:\", float_elements)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sales dataset: [152 202 252 302 352]\n",
      "Sales after tax: [162.64 216.14 269.64 323.14 376.64]\n",
      "Sales after discounting: [144.4, 191.89999999999998, 226.8, 271.8, 316.8]\n",
      "Adjusted sales for 3 weeks:\n",
      " [[152.     202.     252.     302.     352.    ]\n",
      " [155.04   206.04   257.04   308.04   359.04  ]\n",
      " [158.1408 210.1608 262.1808 314.2008 366.2208]]\n"
     ]
    }
   ],
   "source": [
    "X = ord('E') + ord('S')\n",
    "sales = np.array([X, X + 50, X + 100, X + 150, X + 200])\n",
    "print(\"Sales dataset:\", sales)\n",
    "\n",
    "tax_rate = ((X % 5) + 5) / 100\n",
    "sales_after_tax = sales * (1 + tax_rate)\n",
    "print(\"Sales after tax:\", sales_after_tax)\n",
    "\n",
    "discounted_sales=[]\n",
    "for sale in sales:\n",
    "    if sale < X + 100:\n",
    "        discounted_sales.append(sale * 0.95)\n",
    "    elif sale >= X + 100:\n",
    "        discounted_sales.append(sale * 0.90) \n",
    "print(\"Sales after discounting:\",discounted_sales)\n",
    "\n",
    "weeks = 3\n",
    "weekly_sales = np.vstack([sales] * weeks)\n",
    "growth_factor = 1.02 ** np.arange(weeks)[:, None]\n",
    "weekly_sales_adjusted = weekly_sales * growth_factor\n",
    "\n",
    "print(\"Adjusted sales for 3 weeks:\\n\", weekly_sales_adjusted)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "x = np.linspace(-10, 10, 100)\n",
    "\n",
    "y1 = x**2               \n",
    "y2 = np.sin(x)           \n",
    "y3 = np.exp(x)          \n",
    "y4 = np.log(np.abs(x) + 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {

      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(x, y1, label=\"y = x^2\", color='blue')\n",
    "plt.title(\"y = x^2\")\n",
    "plt.xlabel(\"x\")\n",
    "plt.ylabel(\"y\")\n",
    "plt.grid(True)\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
     
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(x, y2, label=\"y = sin(x)\", color='red')\n",
    "plt.title(\"y = sin(x)\")\n",
    "plt.xlabel(\"x\")\n",
    "plt.ylabel(\"y\")\n",
    "plt.grid(True)\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(x, y3, label=\"y = e^x\", color='lime')\n",
    "plt.title(\"y = e^x\")\n",
    "plt.xlabel(\"x\")\n",
    "plt.ylabel(\"y\")\n",
    "plt.grid(True)\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
    
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(x, y4, label=\"y = log(|x| + 1)\", color='cyan')\n",
    "plt.title(\"y = log(|x| + 1)\")\n",
    "plt.xlabel(\"x\")\n",
    "plt.ylabel(\"y\")\n",
    "plt.grid(True)\n",
    "\n",
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