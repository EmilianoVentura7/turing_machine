import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)  # Convierte la cadena de entrada en una lista
        self.head = 0  # Posición inicial de la cabeza
        self.state = 'q0'  # Estado inicial
        self.accepted = False  # Bandera de aceptación

    def get_tape(self):
        return ''.join(self.tape)  # Devuelve el contenido del tape como una cadena

    def is_accepted(self):
        return self.accepted  # Comprueba si la cadena fue aceptada

    def run(self):
        steps = 0  # Contador de pasos para evitar bucles infinitos
        max_steps = 1000  # Límite de pasos para evitar bloqueos

        while self.state != 'q4' and self.state != 'q_reject' and steps < max_steps:
            current_symbol = self.tape[self.head]

            if self.state == 'q0':
                if current_symbol == '0':  # Procesar 0 en estado q0
                    self.tape[self.head] = 'X'  # Reemplaza 0 con X
                    self.head += 1  # Mueve la cabeza a la derecha
                    self.state = 'q1'  # Cambia a q1
                elif current_symbol == 'Y':  # Si encuentra un Y, sigue adelante
                    self.head += 1
                elif current_symbol == ' ':  # Si llega al espacio, aceptar
                    self.state = 'q4'  # Estado final de aceptación

            elif self.state == 'q1':
                if current_symbol == '0':  # Encuentra otro 0 y lo deja igual
                    self.head += 1  # Sigue a la derecha
                elif current_symbol == '1':  # Encuentra un 1, lo reemplaza con Y
                    self.tape[self.head] = 'Y'
                    self.head -= 1  # Se mueve a la izquierda
                    self.state = 'q3'  # Cambia al estado q3
                elif current_symbol == 'Y':  # Si encuentra un Y, sigue a la derecha
                    self.head += 1

            elif self.state == 'q3':
                if current_symbol == 'X':  # Encuentra una X y se mueve a la derecha
                    self.head += 1
                    self.state = 'q0'  # Vuelve al estado q0 para seguir procesando
                elif current_symbol == '0' or current_symbol == 'Y':  # Sigue retrocediendo
                    self.head -= 1  # Mueve la cabeza a la izquierda

            elif self.state == 'q2':  # Procesa estado q2
                if current_symbol == 'Y':  # Encuentra un Y y se mueve a la derecha
                    self.head += 1
                elif current_symbol == ' ':  # Si llega al espacio en blanco, acepta
                    self.state = 'q4'

            steps += 1  # Incrementa el contador de pasos

        # Si llega al estado q4, la cadena fue aceptada
        if self.state == 'q4':
            self.accepted = True
        else:
            self.accepted = False

class TuringMachineGUI:
    def __init__(self, master):
        self.master = master
        master.title("Máquina de Turing")

        self.label = tk.Label(master, text="Ingrese la cadena (formato 0^n 1^n):")
        self.label.pack(pady=10)

        self.input_entry = tk.Entry(master, width=40)
        self.input_entry.pack(pady=5)

        self.run_button = tk.Button(master, text="Ejecutar", command=self.run_machine)
        self.run_button.pack(pady=5)

        self.clear_button = tk.Button(master, text="Limpiar", command=self.clear_input)
        self.clear_button.pack(pady=5)

        self.result_label = tk.Label(master, text="", fg="blue")
        self.result_label.pack(pady=10)

    def run_machine(self):
        input_string = self.input_entry.get().strip()

        if not input_string or any(char not in '01' for char in input_string):
            messagebox.showerror("Error", "Cadena no válida. Debe contener solo 0s y 1s.")
            return

        if input_string.count('0') != input_string.count('1') or input_string.count('0') == 0:
            messagebox.showerror("Error", "La cadena debe tener la misma cantidad de 0s y 1s.")
            return

        tape = input_string + ' '  # Añadir espacio en blanco al final
        machine = TuringMachine(tape)
        machine.run()

        if machine.is_accepted():
            result = f"Cadena aceptada: {machine.get_tape().replace(' ', '')}"
        else:
            result = "Cadena no aceptada."
        
        self.result_label.config(text=result)

    def clear_input(self):
        self.input_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    gui = TuringMachineGUI(root)
    root.mainloop()