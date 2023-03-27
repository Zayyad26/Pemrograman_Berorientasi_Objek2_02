class Tanggal:
   def __init__(self, dd, mm, yyyy):
      self.settanggal(dd, mm, yyyy)

   def settanggal(self, dd, mm, yyyy):
      self.dd = dd
      self.mm = mm
      self.yyyy = yyyy

   def __repr__(self):
      return '%d-%d-%d' % (self.dd, self.mm, self.yyyy)


class Waktu:
   def __init__(self, hh, nn, ss):
      self.hh = hh
      self.nn = nn
      self.ss = ss

   def setwaktu(self, hh, nn, ss):
      self.hh = hh
      self.nn = nn
      self.ss = ss

   def __repr__(self):
      return '%d:%d:%d' % (self.hh, self.nn, self.ss)

class dateTime(Tanggal, Waktu):
   def __init__(self, dd, mm, yyyy, hh, nn ,ss):
      Tanggal.__init__(self,dd,mm,yyyy)
      Waktu.__init__(self,hh,nn,ss)

   def __repr__(self):
      return '%s %s' % \
         (Tanggal.__repr__(self),
          Waktu.__repr__(self))

hasil = dateTime(27,3,2023,21,32,44)
print('Sekarang: %s' % repr(hasil))
