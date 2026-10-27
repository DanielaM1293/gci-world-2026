{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNfyUx0qHpkcbFtA4WcBngE",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DanielaM1293/CursoReact/blob/main/Homework1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "Ndm2puH0lRnO"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "\n",
        "\n",
        "def tarea(a):\n",
        "  mi_resultado = a[(a % 5 == 0) & (a % 2 == 1)]\n",
        "  return mi_resultado"
      ]
    }
  ]
}