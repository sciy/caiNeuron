m0 = [ 0.281183333804077 , 0.226481596384809 , 0.247595731942075 , 0.262655568435646 , 0.274534150887547 , 0.277477498767895 , 0.278678820844804 , 0.280114632231687 , 0.280436105451212]
m1 = [ 0.284231539566278 , 0.258562706901650 , 0.277798619829377 , 0.281678962072805 , 0.283580148103216 , 0.284050802198940 , 0.284182439223742 , 0.284216983364680 , 0.284228441602976]
m2 = [ 0.389767770619786 , 0.377033148886130 , 0.387495232231993 , 0.389131778571893 , 0.389702486512111 , 0.389758422016121 , 0.389766654836214 , 0.389767593410931 , 0.389767747238174]
m3 = [ 0.728165019183702 , 0.716670234210104 , 0.727232706293705 , 0.728098699829870 , 0.728156712578007 , 0.728164461210343 , 0.728164998908043 , 0.728165019126392 , 0.728165019603723]
m4 = [ 0.602504849317523 , 0.591685530725147 , 0.601734658593163 , 0.602474398762176 , 0.602504223335671 , 0.602504828094595 , 0.602504849087696 , 0.602504849829000 , 0.602504849896513]
m5 = [ 0.175578230761065 , 0.175573571998195 , 0.175577947738283 , 0.175578214130320 , 0.175578230531152 , 0.175578231542204 , 0.175578231622087 , 0.175578231594010 , 0.175578231659159]

t_len = len(m5)
t_start = 0.001
ts_list=[]

for i in range(1,t_len):
    m0[i] = fabs(m0[i] - m0[0])
    if (m0[i]>0.5): m0[i] = 1 - m0[i]
    m1[i] = fabs(m1[i] - m1[0])
    if (m1[i]>0.5): m1[i] = 1 - m1[i]
    m2[i] = fabs(m2[i] - m2[0])
    if (m2[i]>0.5): m2[i] = 1 - m2[i]
    m3[i] = fabs(m3[i] - m3[0])
    if (m3[i]>0.5): m3[i] = 1 - m3[i]
    m4[i] = fabs(m4[i] - m4[0])
    if (m4[i]>0.5): m4[i] = 1 - m4[i]
    m5[i] = fabs(m5[i] - m5[0])
    if (m5[i]>0.5): m5[i] = 1 - m5[i]

m0=m0[1:]
m1=m1[1:]
m2=m2[1:]
m3=m3[1:]
m4=m4[1:]
m5=m5[1:]

for i in range(t_len-1): ts_list.append(t_start / 2**i)

for i in range(t_len-1):
    ts_list[i]=log10(ts_list[i])
    m0[i]=log10(m0[i])
    m1[i]=log10(m1[i])
    m2[i]=log10(m2[i])
    m3[i]=log10(m3[i])
    m4[i]=log10(m4[i])
    m5[i]=log10(m5[i])

figure()
plot(ts_list, m0, '.-', label='m=0')
plot(ts_list, m1, '+-', label='m=1')
plot(ts_list, m2, '_-', label='m=2')
plot(ts_list, m3, 'o-', label='m=3')
plot(ts_list, m4, 'x-', label='m=4')
plot(ts_list, m5, '*-', label='m=5')

xlabel("$\log_{10}$(time_step)")
ylabel("$\log_{10}$(error)")
legend(loc='best')
savefig('m_error_list.pdf', dpi=600)
