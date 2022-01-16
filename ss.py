from logging import debug
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('default.html')

@app.route('/menuadmin')
def menuadmin():
    return render_template('menuadmin.html')

@app.route('/menudatamitra')
def menudatamitra():
    return render_template('menudatamitra.html')

@app.route('/menulolist')
def menulolist():
    return render_template('menulolist.html')

@app.route('/inputpendapatan')
def inputpendapatan():
    return render_template('inputpendapatan.html')

@app.route('/inputpengeluaran')
def inputpengeluaran():
    return render_template('inputpengeluaran.html')

@app.route('/inputkasspbe')
def inputkasspbe():
    return render_template('inputkasspbe.html')

@app.route('/inputdatakaryawan')
def inputdatakaryawan():
    return render_template('inputdatakaryawan.html')

@app.route('/inputpolist')
def inputpolist():
    return render_template('inputpolist.html')

@app.route('/inputinvoice')
def inputinvoice():
    return render_template('inputinvoice.html')

@app.route('/inputgajikaryawan')
def inputgajikaryawan():
    return render_template('inputgajikaryawan.html')

@app.route('/inputpenerimaanlpg')
def inputpenerimaanlpg():
    return render_template('inputpenerimaanlpg.html')

@app.route('/inputpenyaluranlpg')
def inputpenyaluranlpg():
    return render_template('inputpenyaluranlpg.html')

@app.route('/inputgain')
def inputgain():
    return render_template('inputgain.html')

@app.route('/depopoint')
def depopoint():
    return render_template('depopoint.html')

@app.route('/transporter')
def transporter():
    return render_template('transporter.html')

@app.route('/agenlpg')
def agenlpg():
    return render_template('agenlpg.html')

@app.route('/supplier')
def supplier():
    return render_template('supplier.html')

@app.route('/stockin')
def stockin():
    return render_template('stockin.html')

@app.route('/stockout')
def stockout():
    return render_template('stockout.html')

@app.route('/stockitem')
def stockitem():
    return render_template('stockitem.html')
    
@app.route('/realstocktank')
def realstocktank():
    return render_template('realstocktank.html')

if __name__ =="__main__":
    app.run(debug = True)