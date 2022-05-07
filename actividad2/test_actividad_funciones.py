import pytest
import actividad_funciones as af
import pandas as pd

def test_validarColumnas():
    assert af.validarColumnas(df) == columns

def test_validarNumeroColumnas():
    assert af.validarNumeroColumnas(df,12) == True

def test_validarCampos():
    assert af.validarCampos(df,columns,0)

df = af.abrirArchivo()
columns = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio',
         'Agosto','Septiembre','Octubre','Noviembre','Diciembre']