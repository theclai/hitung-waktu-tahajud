from termcolor import colored

def hitung_tahajud(ih, im, fh, fm):
    i = (ih) * 60 + im
    f = (fh + 12) * 60 + fm

    td = (f - i) / 3
    tahajud = i + 2 * td

    return tahajud


def hitungAmPm(t):
    d = dict()

    if t >= 720:
        hr = t / 60 - 12
        if hr < 1:
            hr = 12
        mn = t % 60
        ampm = 'A'
    else:
        hr = t / 60
        if hr < 1:
            hr = 12
        mn = t % 60
        ampm = 'P'

    d['hr'] = hr
    d['mn'] = mn
    d['ampm'] = ampm

    return d


def tampilkan_hasil_perhitungan(d):
    hr = int(d['hr'])
    mn = int(d['mn'])
    ampm = d['ampm']

    result = ""

    if hr < 10:
        result += '0%d:' % hr
    else:
        result += '%d:' % hr
    if mn < 10:
        result += '0%d:' % mn
    else:
        result += '%d' % mn

    result += ' %sM' % ampm
    print("Waktu sholat tahajud pada jam " + result)


if __name__ == '__main__':
    print(" ")
    print(colored("\n[+] Program menghitung waktu sholat tahajud", "red",
                  attrs=['bold']))
    isha = input(colored("[+] Masukan waktu sholat Isha (jam:menit) : ", 'blue', attrs=['bold']))
    subuh = input(colored("[+] Masukan waktu sholat Subuh (jam:menit) : ", 'blue', attrs=['bold']))

    ishaHr, ishaMn = [int(i) for i in isha.split(":")]
    subuhHr, subuhMn = [int(i) for i in subuh.split(":")]

    t = hitung_tahajud(ishaHr, ishaMn, subuhHr, subuhMn)
    tampilkan_hasil_perhitungan(hitungAmPm(t))
