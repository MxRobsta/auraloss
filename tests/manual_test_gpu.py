import torch
import RobAuraLoss

y_hat = torch.randn(2, 1, 131072)
y = torch.randn(2, 1, 131072)

loss_fn = RobAuraLoss.freq.MelSTFTLoss(44100)
loss_fn2 = RobAuraLoss.freq.MultiResolutionSTFTLoss()

# loss_fn.cuda()

y_hat = y_hat.cuda()
y = y.cuda()

loss = loss_fn2(y_hat, y)
loss = loss_fn(y_hat, y)
