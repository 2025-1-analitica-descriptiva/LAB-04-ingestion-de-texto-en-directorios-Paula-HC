# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    file "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este file.

    Como resultado se creara la carpeta "input" en la root del
    repositorio, la cual contiene la siguiente estructura de files:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos files llamados "train_dataset.csv" y "test_dataset.csv". Estos
    files deben estar ubicados en la carpeta "output" ubicada en la root
    del repositorio.

    Estos files deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada file de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el file.

    Cada file tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    import os
    import pandas as pd
    import zipfile

    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    rut_in = os.path.join(root, 'input')
    
    fol_out = os.path.join(root, 'files', 'output')
    
    os.makedirs(fol_out, exist_ok=True)

    ar_zip = os.path.join(root, 'files', 'input.zip')
    
    if not os.path.isdir(rut_in):
        with zipfile.ZipFile(ar_zip, 'r') as file:
            file.extractall(root)

    def cargar_textos(nombre_carpeta):
    
        regis = []
    
        catg = ['positive', 'negative', 'neutral']
    
        for clase in catg:
    
            ubicacion = os.path.join(rut_in, nombre_carpeta, clase)
    
            if not os.path.isdir(ubicacion):
                continue
    
            for name_file in os.listdir(ubicacion):
    
                if name_file.endswith('.txt'):
                    file_txt = os.path.join(ubicacion, name_file)
    
                    with open(file_txt, encoding='utf-8') as texto:
                        cont = texto.read().strip()
                        regis.append({'phrase': cont, 'target': clase})
    
        return regis

    for particion in ['train', 'test']:
        conj = cargar_textos(particion)
        table = pd.DataFrame(conj)
        table.to_csv(os.path.join(fol_out, f'{particion}_dataset.csv'), index=False)