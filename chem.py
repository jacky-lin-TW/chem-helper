# 原子量表：IUPAC CIAAW Abridged Standard Atomic Weights 2024
atomic_mass = {
    "H": 1.0080, "He": 4.0026, "Li": 6.94, "Be": 9.0122, "B": 10.81,
    "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998, "Ne": 20.180,
    "Na": 22.990, "Mg": 24.305, "Al": 26.982, "Si": 28.085, "P": 30.974,
    "S": 32.06, "Cl": 35.45, "Ar": 39.95, "K": 39.098, "Ca": 40.078,
    "Sc": 44.956, "Ti": 47.867, "V": 50.942, "Cr": 51.996, "Mn": 54.938,
    "Fe": 55.845, "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.38,
    "Ga": 69.723, "Ge": 72.630, "As": 74.922, "Se": 78.971, "Br": 79.904,
    "Kr": 83.798, "Rb": 85.468, "Sr": 87.62, "Y": 88.906, "Zr": 91.222,
    "Nb": 92.906, "Mo": 95.95, "Ru": 101.07, "Rh": 102.91, "Pd": 106.42,
    "Ag": 107.87, "Cd": 112.41, "In": 114.82, "Sn": 118.71, "Sb": 121.76,
    "Te": 127.60, "I": 126.90, "Xe": 131.29, "Cs": 132.91, "Ba": 137.33,
    "La": 138.91, "Ce": 140.12, "Pr": 140.91, "Nd": 144.24, "Sm": 150.36,
    "Eu": 151.96, "Gd": 157.25, "Tb": 158.93, "Dy": 162.50, "Ho": 164.93,
    "Er": 167.26, "Tm": 168.93, "Yb": 173.05, "Lu": 174.97, "Hf": 178.49,
    "Ta": 180.95, "W": 183.84, "Re": 186.21, "Os": 190.23, "Ir": 192.22,
    "Pt": 195.08, "Au": 196.97, "Hg": 200.59, "Tl": 204.38, "Pb": 207.2,
    "Bi": 208.98, "Th": 232.04, "Pa": 231.04, "U": 238.03,
}
            
formula = input("請輸入化學式：")   # 讓使用者打化學式，例如 CH3COOH
counts = {}      # 空字典，用來記每種元素有幾個
symbol = ""      # 正在讀的元素符號，例如 "C"、"Na"
number = ""      # 正在讀的數字，先用字串存，例如 "12"

for ch in formula:                 # 一個字一個字讀化學式
    if ch.isupper():               # 大寫字母：新元素開始了
        if symbol != "":           # 如果前面已經有讀完的元素
            if number == "":       # 元素後面沒寫數字
                number = "1"       # 就代表 1 個
            counts[symbol] = counts.get(symbol, 0) + int(number)   # 把上一個元素「加」進字典（查不到當 0）
        symbol = ch                # 開始讀新元素
        number = ""                # 數字歸零，重新讀
    elif ch.islower():             # 小寫字母：元素符號的第二個字
        symbol = symbol + ch       # 接起來，例如 "N" + "a" = "Na"
    elif ch.isdigit():             # 數字：這個元素的個數
        number = number + ch       # 接起來，例如 "1" + "2" = "12"

# 迴圈結束後，最後一個元素還沒存，要補存一次
if number == "":
    number = "1"
counts[symbol] = counts.get(symbol, 0) + int(number)

print(counts)    # 印出結果，例如 {'C': 2, 'H': 4, 'O': 2}
missing = []                            # 空串列，用來裝「表裡查不到的元素」
for symbol in counts:                   # 先檢查每個元素
    if symbol not in atomic_mass:       # 原子量表裡沒有這個元素
        missing.append(symbol)          # 把它放進 missing

if len(missing) > 0:                                  # 有查不到的元素
    print(f"原子量表裡還沒有這些元素：{missing}")
else:                                                 # ← 就是這個 else：全部查得到才算
    total = 0
    for symbol in counts:
        total = total + atomic_mass[symbol] * counts[symbol]
    print(f"{formula} 的分子量是 {round(total, 3)} g/mol")

    mode = input("要算什麼？1 = 公克換濃度，2 = 配溶液要秤幾公克：")   # 選單

    if mode == "1":                                   # 選 1：公克 → 莫耳 → 濃度
        grams = float(input("有幾公克？"))
        moles = grams / total                         # n = m ÷ M
        print(f"{grams} g 的 {formula} = {round(moles, 4)} mol")
        ml = float(input("溶液體積幾毫升？"))
        liters = ml / 1000                            # 毫升換公升
        molarity = moles / liters                     # C = n ÷ V
        print(f"濃度 = {round(molarity, 4)} M (mol/L)")
    elif mode == "2":                                 # 選 2：配溶液要秤幾公克
        target_m = float(input("要配幾 M？"))
        target_ml = float(input("要配幾毫升？"))
        need = target_m * (target_ml / 1000) * total  # m = C × V × M
        print(f"要秤 {round(need, 4)} g 的 {formula}")
    else:                                             # 打了 1、2 以外的東西
        print("請輸入 1 或 2")
