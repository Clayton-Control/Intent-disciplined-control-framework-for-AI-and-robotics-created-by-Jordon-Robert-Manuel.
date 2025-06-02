# Clayton Control Model
# Created by Jordon Robert Manuel
# Licensed under PolyForm Noncommercial + CLAYTON_USE.md
# Rhythm-critical system — unauthorized commercial use prohibited


import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6 * np.pi, 300)
R = 0.6 + 0.4 * np.sin(2 * t) + 0.1 * np.random.randn(300)
B = np.sin(0.5 * t)
theta_sync = 0.2
allowed = (R * B) > theta_sync
raw = np.cos(3 * t) + 0.3 * np.random.randn(300)
gated = np.where(allowed, raw, np.nan)

fig, axs = plt.subplots(3, 1, figsize=(12, 9), sharex=True)
axs[0].plot(t, raw, label="Raw Output", color="gray", alpha=0.6)
axs[1].plot(t, R * B, label="Gate Signal", color="purple")
axs[1].axhline(theta_sync, color="red", linestyle="--")
axs[2].plot(t, gated, label="Gated Output", color="green")
for ax in axs: ax.legend()
axs[-1].set_xlabel("Time")
plt.tight_layout()
plt.show()