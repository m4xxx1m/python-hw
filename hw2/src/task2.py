from generate_latex_m4xxx1m import (generate_table, generate_image, generate_latex)

if __name__ == "__main__":
    table = generate_table([
        ['ID', 'firstname', 'lastname', 'zip', 'city'],
        [1, 'Max', 'Jones', 14482, 'Potsdam'],
        [2, 'Max', 'Miller', 14482, 'Potsdam'],
        [3, 'Max', 'Jones', 10115, 'Berlin'],
        [4, 'Anna', 'Scott', 13591, 'Berlin'],
        [5, 'Marie', 'Scott', 14467, 'Potsdam'],
        [6, 'Marie', 'Gray', 14469, 'Potsda'],
    ])

    image = generate_image('images/image.png', '8cm')

    latex = generate_latex([table, image])

    with open('output/document.tex', 'w') as file:
        file.write(latex)
