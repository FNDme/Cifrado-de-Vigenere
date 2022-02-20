# Cifrado de Vigenere

El cifrado de Vigenere es un sistema de cifrado polialfabético usado para alternar el empleo de las sustituciones-clave durante la operación de cifrado. Con esta técnica, la misma letra de origen se transforma en distintas letras cifradas, en función de la posición que ocupa dentro del mensaje.

## Utilización
```
python GUI.py
```

## Cómo funciona

El cifrado de Vigenere se puede aplicar utilizando el siguiente cuadro:

```
A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z
B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z A
C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z A B
D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z A B C
E F G H I J K L M N Ñ O P Q R S T U V W X Y Z A B C D
F G H I J K L M N Ñ O P Q R S T U V W X Y Z A B C D E
G H I J K L M N Ñ O P Q R S T U V W X Y Z A B C D E F
H I J K L M N Ñ O P Q R S T U V W X Y Z A B C D E F G
I J K L M N Ñ O P Q R S T U V W X Y Z A B C D E F G H
J K L M N Ñ O P Q R S T U V W X Y Z A B C D E F G H I
K L M N Ñ O P Q R S T U V W X Y Z A B C D E F G H I J
L M N Ñ O P Q R S T U V W X Y Z A B C D E F G H I J K
M N Ñ O P Q R S T U V W X Y Z A B C D E F G H I J K L
N Ñ O P Q R S T U V W X Y Z A B C D E F G H I J K L M
Ñ O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
O P Q R S T U V W X Y Z A B C D E F G H I J K L M N Ñ
P Q R S T U V W X Y Z A B C D E F G H I J K L M N Ñ O
Q R S T U V W X Y Z A B C D E F G H I J K L M N Ñ O P
R S T U V W X Y Z A B C D E F G H I J K L M N Ñ O P S
S T U V W X Y Z A B C D E F G H I J K L M N Ñ O P Q R
T U V W X Y Z A B C D E F G H I J K L M N Ñ O P Q R S
U V W X Y Z A B C D E F G H I J K L M N Ñ O P Q R S T
V W X Y Z A B C D E F G H I J K L M N Ñ O P Q R S T U
W X Y Z A B C D E F G H I J K L M N Ñ O P Q R S T U V
X Y Z A B C D E F G H I J K L M N Ñ O P Q R S T U V W
Y Z A B C D E F G H I J K L M N Ñ O P Q R S T U V W X
Z A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y
```
En este cifrado, se hace uso de una palabra-clave. Para explicar el funcionamiento, observemos el siguiente ejemplo, donde la palabra-clave es `"LOREM"`:

- EL-PAPA-SERA-TRAICIONADO
- LO-REML-OREM-LOREMLOREML

En este caso, la clave se termina por truncar, y no cifraremos los espacios en blanco. Si vamos a cifrar, la primera letra del mensaje la buscaremos en la primera fila, y la primera letra de la clave en la primera columna. Si buscamos la intersección entre ambas, nos dará la letra cifrada.

Si repetimos la operación, obtenemos el siguiente mensaje cifrado:

- PZ GEBL GVVM EFRMOTCEEPZ

## Contribuir
Las solicitudes de modificación son bienvenidas. Para los cambios importantes, por favor, abra una cuestión en primer lugar para discutir lo que le gustaría cambiar.

Por favor, asegúrese de actualizar las pruebas según corresponda.