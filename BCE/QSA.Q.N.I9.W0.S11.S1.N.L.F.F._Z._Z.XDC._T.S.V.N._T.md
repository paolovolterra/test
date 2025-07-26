# QSA.Q.N.I9.W0.S11.S1.N.L.F.F._Z._Z.XDC._T.S.V.N._T

  
Total financial **liabilities** of Non financial corporations, Euro area 20 (fixed composition), Quarterly
https://data.ecb.europa.eu/data/datasets/QSA/QSA.Q.N.I9.W0.S11.S1.N.L.F.F._Z._Z.XDC._T.S.V.N._T


|Codice componente|Significato|
|---|---|
|`QSA`|Quarterly Sector Accounts|
|`Q`|Frequenza: Trimestrale|
|`N`|Nessun aggiustamento stagionale|
|`I9`|Area Euro (19 paesi)|
|`W0`|Tutte le controparti (mondo intero)|
|`S11`|Società non finanziarie|
|`S1`|Controparte: economia totale|
|`N`|Non consolidato|
|`L`|Passività|
|`F`|Flussi finanziari (Transazioni)|
|`F.F.`|Tutti gli strumenti finanziari|
|`_Z._Z.`|Nessuna ripartizione COFOG/COICOP|
|`XDC`|Valuta domestica|
|`_T`|Tutte le valute|
|`S`|Valutazione standard|
|`V`|Valore osservato|
|`N`|Nessuna trasformazione|
|`_T`|Totale|

---

### ⚠️ Attenzione: **questa serie mostra i flussi di passività finanziarie (non gli stock!)**

**Cosa rappresenta?**

> Le **transazioni finanziarie trimestrali** in **passività** delle società non finanziarie dell’**area euro (I9)**, **per tutti gli strumenti** (prestiti, obbligazioni, ecc.), in **valori assoluti (milioni di euro)**.

---

## ❌ Non adatta per il tuo grafico

Stai cercando la **composizione del debito finanziario** – servono **stock** per:

- **Loans (F.4)**
    
- **Debt securities (F.3)**
    

---

## ✅ Serie corrette da cercare:

|Componente|Codice serie|Area|
|---|---|---|
|**Prestiti (F.4)**|`QSA.A.N.IT.W0.S11.S1.N.L.LE.F4._Z._Z.XDC._T.S.V.N._T`|Italia|
|**Obbligazioni (F.3)**|`QSA.A.N.IT.W0.S11.S1.N.L.LE.F3._Z._Z.XDC._T.S.V.N._T`|Italia|

> Sostituisci `IT` con `FR`, `DE`, `I9` per Francia, Germania, Area euro.

---

Vuoi che ti fornisca un file CSV con queste serie già raccolte (anni 2007, 2021, 2024) oppure uno script Python per automatizzare l’estrazione e calcolo delle percentuali?