from fractions import Fraction
# 先验概率男
# 男人的概率
p_y_man = Fraction(2, 3)
# 女人概率
p_y_woman = Fraction(1, 3)
# 公园男人穿凉鞋的概率
p_x_x1_y_man = Fraction(1, 2)
# 公园女人穿凉鞋的概率
p_x_x1_y_woman = Fraction(2, 3)
# 基于全概率公式下求得穿凉鞋的概率
p_X_x1=p_y_man*p_x_x1_y_man+p_y_woman*p_x_x1_y_woman
# 基于全概率公式下求得不穿凉鞋的概率
p_X_x0 = p_y_man*(1-p_x_x1_y_man)+p_y_woman*(1-p_x_x1_y_woman)
# 基于贝叶斯公式下求得穿凉鞋为男生/女生的概率
p_ym_x1=(p_x_x1_y_man*p_y_man)/p_X_x1
p_yw_x1=(p_x_x1_y_woman*p_y_woman)/p_X_x1
print("男生穿凉鞋概率：")
print(p_ym_x1)
print("女生穿凉鞋概率：")
print(p_yw_x1)

