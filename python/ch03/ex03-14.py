# 例3-14 x値からZスコアを求め、それを元に戻す例

def z_score(x, mean, std):
    return (x - mean) / std


def z_to_x(z, mean, std):
    return (z * std) + mean


mean = 140000
std_dev = 3000
x = 150000

# Zスコアを求めてxに戻す
z = z_score(x, mean, std_dev)
back_to_x = z_to_x(z, mean, std_dev)

print("Zスコア: {}".format(z))
print("xに戻す: {}".format(back_to_x))
