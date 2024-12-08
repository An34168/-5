import re
text = """
We start by presenting one of the simplest circulation observables, that is, the variance of the circulation for loops of different sizes in quantum turbulence. The scaling of the circulation with the area of the loops is displayed in Fig. 2. For comparison purposes, we also perform direct
numerical simulations of the Navier-Stokes equations (see Appendix C). We then compute the scaling of the circulation variance in the steady state at a Taylor-scale Reynolds number of Reλ ≈ 320.
"""
capitalized_words = re.findall(r'\b[A-Z][a-z]*\b', text)
words_before_colon = re.findall(r'\b\w+(?=:\s*)', text)
result = list(set(capitalized_words + words_before_colon))

print("Найденные слова:")
for word in sorted(result):
    print(word)
