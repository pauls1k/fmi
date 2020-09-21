#include <iostream>
#include<stdlib.h>

using namespace std;


class Persoana{
protected:
    int id;
    string nume;
    string cnp;
    static int n;
public:

    ///  constructori
    Persoana();
    Persoana(int id, string nume, string cnp);
    Persoana(Persoana& ob);
    ~Persoana();


    ///  supraincarcari
    friend istream& operator>>(istream& in, Persoana& ob);
    friend ostream& operator<<(ostream& out, Persoana& ob);
    Persoana& operator=(Persoana& ob);

    ///
    virtual void citire(istream &in);
    virtual void afisare(ostream &out);

    friend class Clienti;

    static void numarAbonati(){
        cout<<"Lista contine "<< n << " abonati.";
    }
};

int Persoana::n;

Persoana::Persoana(){
    n++;
    id = 0;
    nume = "";
    cnp = "";
}

Persoana::Persoana(int id, string nume, string cnp){
    this->id = id;
    this->nume = nume;
    this->cnp = cnp;
}

Persoana::Persoana(Persoana& ob){
    this->id = ob.id;
    this->nume = ob.nume;
    this->cnp = ob.cnp;
}

Persoana::~Persoana(){
    id = 0;
    nume = "";
    cnp = "";
}

void Persoana::citire(istream &in){
    cout<<"Id persoana:"<<endl;
    in>>id;
    cout<<"Nume persoana:"<<endl;
    in.get();
    getline(in, nume);
    cout<<"CNP persoana:"<<endl;
    in>>cnp;
}

istream& operator>>(istream& in, Persoana& ob){
    ob.citire(in);
    return in;
}

void Persoana::afisare(ostream &out){
    out<<id<<". "<<nume<<endl;
    out<<"CNP: "<<cnp<<endl;
}

ostream& operator<<(ostream& out, Persoana& ob){
    ob.afisare(out);
    return out;
}

Persoana& Persoana::operator=(Persoana& ob){
    id = ob.id;
    nume = ob.nume;
    cnp = ob.cnp;

    return * this;
}




class Abonament{
protected:
    string nume_abonament;
    float pret;
    int perioada;
public:

    ///  constructori
    Abonament();
    Abonament(string nume_abonament, float pret, int perioada);
    Abonament(Abonament& ob);
    ~Abonament();

    ///  supraincarcari
    friend istream& operator>>(istream& in, Abonament& ob);
    friend ostream& operator<<(ostream& out, Abonament& ob);
    Abonament& operator=(Abonament& ob);

    virtual void citire(istream &in);
    virtual void afisare(ostream &out);

    friend class Clienti;
};

Abonament::Abonament(){
    nume_abonament = "";
    pret = 0;
    perioada = 0;
}

Abonament::Abonament(string nume_abonament, float pret, int perioada){
    this->nume_abonament = nume_abonament;
    this->pret = pret;
    this->perioada = perioada;
}

Abonament::Abonament(Abonament& ob){
    this->nume_abonament = ob.nume_abonament;
    this->pret = ob.pret;
    this->perioada = ob.perioada;
}

Abonament::~Abonament(){
    nume_abonament = "";
    pret = 0;
    perioada = 0;
}

void Abonament::citire(istream &in){
    cout<<"Nume abonament: "<<endl;
    in.get();
    getline(in, nume_abonament);
    cout<<"Pret abonament: "<<endl;
    in>>pret;
    cout<<"Perioada abonament: "<<endl;
    in>>perioada;
}

istream& operator>>(istream& in, Abonament& ob){
    ob.citire(in);
    return in;
}

void Abonament::afisare(ostream &out){
    out<<"Nume abonament: "<<nume_abonament<<", "<<"Pret: "<<pret<<", Perioada: "<<perioada<<endl;
}

ostream& operator<<(ostream& out, Abonament& ob){
    ob.afisare(out);
    return out;
}

Abonament& Abonament::operator=(Abonament& ob){
    nume_abonament = ob.nume_abonament;
    pret = ob.pret;
    perioada = ob.perioada;

    return * this;
}

class Abonament_premium:public Abonament{
    int reducere;
public:
    /// constructori
    Abonament_premium();
    Abonament_premium(int reducere);
    Abonament_premium(Abonament_premium& ob);
    ~Abonament_premium();

    ///  supraincarcare
    friend istream& operator>>(istream& in, Abonament_premium& ob);
    friend ostream& operator<<(ostream& out, Abonament_premium& ob);
    Abonament_premium& operator=(Abonament_premium& ob);

    ///
    void citire(istream &in);
    void afisare(ostream &out);

    friend class Clienti;
};

Abonament_premium::Abonament_premium():Abonament(){
    this->reducere = 0;
}

Abonament_premium::Abonament_premium(int reducere):Abonament(nume_abonament,pret,perioada){
    this->reducere = reducere;
}

Abonament_premium::Abonament_premium(Abonament_premium& ob){
    reducere = ob.reducere;
}

Abonament_premium::~Abonament_premium(){
    this->reducere = 0;
}

void Abonament_premium::citire(istream &in){
    Abonament::citire(in);
    cout<<"Reducere: "<<endl;
    in>>reducere;
}

istream& operator>>(istream& in, Abonament_premium &ob){
    ob.citire(in);
    return in;
}

void Abonament_premium::afisare(ostream &out){
    Abonament::afisare(out);
    out<<"Reducere: "<<reducere<<endl;
}

ostream& operator<<(ostream& out, Abonament_premium& ob){
    ob.afisare(out);
    return out;
}

Abonament_premium& Abonament_premium::operator=(Abonament_premium& ob){
    reducere = ob.reducere;

    return * this;
}

class Abonat: public Persoana{
    string nr_telefon;
    Abonament_premium a;
public:

    /// constructori
    Abonat();
    Abonat(string nr_telefon, Abonament_premium);
    Abonat(Abonat& ob);
    ~Abonat();

    /// supraincarcare
    friend istream& operator>>(istream& in, Abonat& ob);
    friend ostream& operator<<(ostream& out, Abonat& ob);
    Abonat& operator=(Abonat& ob);

    ///
    void citire(istream &in);
    void afisare(ostream &out);

    friend class Clienti;
};



Abonat::Abonat():Persoana(){
    this->nr_telefon = "";
    Abonament a();
}

Abonat::Abonat(string nr_telefon, Abonament_premium ab):Persoana(id, nume, cnp){
    this->nr_telefon = nr_telefon;
    Abonament a(ab);
}

Abonat::Abonat(Abonat& ob){
    nr_telefon = ob.nr_telefon;
}

Abonat::~Abonat(){
    this->nr_telefon = "";
    delete &a;
}

void Abonat::citire(istream &in){
    Persoana::citire(in);
    cout<< "Nr.Telefon: "<<endl;
    in>>nr_telefon;
    in>>a;
}

istream& operator>>(istream& in, Abonat &ob){
    ob.citire(in);
    return in;
}

void Abonat::afisare(ostream &out){
    Persoana::afisare(out);
    out<<"Numar Telefon: "<<nr_telefon<<endl;
    out<<a<<endl;
}

ostream& operator<<(ostream& out, Abonat& ob){
    ob.afisare(out);
    return out;
}

Abonat& Abonat::operator=(Abonat& ob){
    nr_telefon = ob.nr_telefon;
    return * this;
}




class Clienti{
    int n;
    Abonat *a;
public:
    Clienti();                    ///  constructor initializare
    Clienti(int);              ///  constructor parametrizat
    Clienti(Clienti &ob);        ///  constructor copiere
    ~Clienti();             ///  destructor

    /// supraincarcare
    friend istream& operator>>(istream& in, Clienti &ob);
    friend ostream& operator<<(ostream& out, Clienti &ob);
    Clienti& operator=(Clienti& ob);


    ///
    void citire(istream &in);
    void afisare(ostream &out);


    ///  functie care calculeaza abonatii premium - verifica daca reducerea este diferita de 0 ( reducere == 0 ->abonat simplu )
    void premiumCount(){
        int cc = 0;
        for(int i = 0;i<n;i++){
            if(a[i].a.reducere){
                cc++;
            }
        }
        cout<<"Numarul de abonati premium este "<<cc<<endl;
    }


    ///  functie care calculeaza totalul de bani incasati
    void total(){
        int suma = 0;
        for(int i = 0;i<n;i++){
            suma = suma + (a[i].a.pret - (a[i].a.pret*a[i].a.reducere)/100)*a[i].a.perioada;
        }
        cout<<"Suma totala incasata este "<< suma<<endl;
    }

};

Clienti::Clienti(){
    this->n = 0;
    Abonat* a = new Abonat[0];
}

Clienti::Clienti(int n){
    this->n = n;
    Abonat* a = new Abonat[n];
}


Clienti::Clienti(Clienti &ob){
    n = ob.n;
    Abonat* a = new Abonat[ob.n];
    for(int i=0;i<ob.n;i++){
        a[i] = ob.a[i];
    }
}

Clienti::~Clienti(){
    n = 0;
    delete []a;
}

void Clienti::citire(istream &in){
    cout<<"Numat de abonati: "<<endl;
    in>>n;
    a = new Abonat[n];
    for(int i = 0;i<n;i++){
        in>>a[i];
    }
}

istream& operator>>(istream& in, Clienti &ob){
    ob.citire(in);
    return in;
}

void Clienti::afisare(ostream &out){
    for(int i = 0;i<n;i++){
        out<<a[i]<<endl;
    }
}

ostream& operator<<(ostream& out, Clienti &ob){
    ob.afisare(out);
    return out;
}





int main()
{
    int elem,i,ans;
    cout<<"\n\nNumar de obiecte: ";
    cin>>elem;
    Clienti *c = new Clienti[elem];

    for(i = 0; i<elem+1;i++){
        cout<<"\n\n--> MENU <--"<<endl;
        cout<<"______________________________"<<i+1<<endl;
        cout<<"2.Initializare si citire obiect "<<i+1<<endl;
        cout<<"3.Afiseaza obiect "<<i+1<<endl;
        cout<<"4.Determina numarul de abonati premium "<<i+1<<endl;
        cout<<"5.Suma totala de bani incasata de la abonati "<<i+1<<endl;
        cout<<"0.EXIT "<<endl;
        cout<<"\n\n Obiect "<<i+1<<"\n\n\n";
        do{
            cout<<"\n\nSelecteaza optiune:\n\n";
            cin>>ans;

            switch(ans)
            {
                case 1:
                    {
                        Clienti c[i];
                    }
                    break;
                case 2:
                    cin>>c[i];
                    break;
                case 3:
                    cout<<c[i];
                    break;
                case 4:
                    c[i].premiumCount();
                    break;
                case 5:
                    c[i].total();
                    break;
                default:
                    cout<<"Optiune incorecta"<<endl;

            }
        }while(ans>=1 && ans<=5);

    }
    return 0;
}
