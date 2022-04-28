import pandas as pnd
import JMPEstadisticas as jmp
import numpy as np

observaciones = pnd.DataFrame({'Name: (0)':np.array()}

stats = jmp.JMPEstadisticas(observaciones['Name'])
stats.analisisCaracteristica()