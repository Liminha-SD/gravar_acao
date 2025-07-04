# Gravador de Ações do Mouse

Este script Python permite gravar coordenadas do mouse e associá-las a rótulos personalizados. É útil para automatizar tarefas que envolvem cliques e movimentos do mouse em posições específicas da tela.

## Como Usar

1.  **Execute o script:**
    ```bash
    python gravar_acao.py
    ```

2.  **Grave as ações:**
    *   Mova o mouse para a posição desejada.
    *   Pressione a tecla `s` para salvar a posição atual do mouse.
    *   Quando solicitado, digite um rótulo descritivo para a ação (ex: `clicar_botao_salvar`, `posicao_campo_texto`).

3.  **Finalize a gravação:**
    *   Pressione a tecla `esc` para parar a gravação.

## Saída

As ações gravadas serão salvas no arquivo `recorded_actions.txt` no mesmo diretório do script. Cada linha do arquivo terá o formato:

```
POINT: X,Y LABEL: seu_rotulo_aqui
```

## Comandos Extras no `recorded_actions.txt`

Além dos pontos do mouse, você pode adicionar manualmente comandos de teclado ao arquivo `recorded_actions.txt` para enriquecer a sequência de ações. Use os seguintes formatos:

*   **Pressionar uma tecla:**
    ```
    KEY: <nome_da_tecla>
    ```
    Exemplo: `KEY: enter`, `KEY: esc`, `KEY: tab`

*   **Digitar um texto:**
    ```
    TYPE: <seu_texto_aqui>
    ```
    Exemplo: `TYPE: meu_nome_de_usuario`

*   **Pressionar e segurar uma tecla (para combinações):**
    ```
    KEYDOWN: <nome_da_tecla>
    ```
    Exemplo: `KEYDOWN: ctrl`

*   **Soltar uma tecla:**
    ```
    KEYUP: <nome_da_tecla>
    ```
    Exemplo: `KEYUP: ctrl`

*   **Pausa (em segundos):**
    ```
    SLEEP: <segundos>
    ```
    Exemplo: `SLEEP: 0.5` (pausa de meio segundo)

## Requisitos

Certifique-se de ter as seguintes bibliotecas Python instaladas:

*   `pyautogui`
*   `pynput`

Você pode instalá-las usando pip:

```bash
pip install pyautogui pynput
```
