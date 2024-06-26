#include <iostream>
#include <string.h>
#include <fstream>
#include <windows.h>
#include <cstdio>
#include <ctime>
using namespace std;
#define gt(x,y) ;{COORD a;a.X = x; a.Y = y;SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);}
#define pare gt(2,26); sy("pause");
struct NODO{
     string pag;
     string password;
     string usuario;
     NODO *sig;};
bool listaVacia(NODO *cab){
	return cab==NULL;
	}
void registrarpassword(NODO *&cab, string pag, string usuario, string password){
     NODO *aux= new NODO;
     aux->pag=pag;
     aux->usuario=usuario;
     aux->password=password;
     aux->sig=NULL;
     if(cab==NULL)
          cab=aux;
          else{
               NODO *ult=cab;
               while(ult->sig!=NULL)
               ult=ult->sig;
               ult->sig=aux;
}
}
void mostrarNotas(NODO *aux){
     if(aux==NULL)
          cout<<"Vacia"<<endl;
     else{
          do{
		     cout<<"->Pagina: "<<aux->pag<<"; Usuario: "<<aux->usuario<<"; Password: "<<aux->password<<endl;
			aux=aux->sig;
          }while(aux!=NULL);
          cout<<"\n";}
}
bool grabar(NODO  *cab, char *nf){
ofstream ofs(nf);
if(!ofs)
return false;
while(cab!=NULL){
     ofs<<cab->pag<<endl;
     ofs<<cab->usuario<<endl;
     ofs<<cab->password<<endl;
     cab=cab->sig;
}ofs.close();
     return true;
}
NODO* cargar(char *nf){
     ifstream ifs(nf);
     if(!ifs)
     return NULL;
     NODO *cab=NULL;
     string pag;
     string password;
     string usuario;
     ifs>>pag;
     ifs>>usuario;
     ifs>>password;
     while(!ifs.eof()){
     registrarpassword(cab, pag, usuario, password);
     ifs>>pag;
     ifs>>usuario;
     ifs>>password;
     }ifs.close();
     return cab;
}
int GenerarContrasenaNumerica(){
	srand(time(0));
	int contrasena = 00000000;
	for (int i =0; i < 8; ++i) {
		contrasena = contrasena * 10 + rand() % 10 ;
	}
	gt(11,24);cout<<"Contraseña Numerica Generada: "<<contrasena;
	return 0;
}
string generarContrasenaAlfabetica(int longitud) {
    const string caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string contrasena;
    if (longitud <= 0) {
        cout << "Longitud de contraseña inválida." << endl;
        return contrasena;
    }
    for (int i = 0; i < longitud; ++i) {
        int indiceAleatorio = rand() % caracteres.size();
        contrasena += caracteres[indiceAleatorio];
    }
    gt(11, 24);cout << "Contraseña Alfabetica Generada: " << contrasena << endl;
    return contrasena;
}
string generarContrasenaAlfaNumerica(int longitud) {
    const string caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    string contrasena;
    if (longitud <= 0) {
        cout << "Longitud de contraseña inválida." << endl;
        return contrasena;
    }
    for (int i = 0; i < longitud; ++i) {
        int indiceAleatorio = rand() % caracteres.size();
        contrasena += caracteres[indiceAleatorio];
    }
    gt(11, 24);cout << "Contraseña Alfabetica Generada: " << contrasena << endl;
    return contrasena;
}
string generarContrasenaCadenadeCaracteres(int longitud) {
    const string caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789|°¬!¡#$%&/\()=¿?´´¨¨*+~{}[]^^``<>;,:._-";
    string contrasena;
    if (longitud <= 0) {
        cout << "Longitud de contraseña inválida." << endl;
        return contrasena;
    }
    for (int i = 0; i < longitud; ++i) {
        int indiceAleatorio = rand() % caracteres.size();
        contrasena += caracteres[indiceAleatorio];
    }
    gt(11, 24);cout << "Contraseña Alfabetica Generada: " << contrasena << endl;
    return contrasena;
}
int terminator() {
	gt(11,24);
    const char* archivo = "C:\\Users\\LATINA\\Desktop\\Ingenieria De Sistemas\\Datos_Estudiantes.txt";
    if (std::FILE* file = std::fopen(archivo, "r")) {
        std::fclose(file);
        if (std::remove(archivo) == 0) {
            std::cout << "Archivo Eliminado." << std::endl;
        } else {
            std::cout << "Error Al Eliminar." << std::endl;
        }
    } else {
        std::cout << "No Existe El Archivo" << std::endl;
    }
    return 0;
}
void ventanamostrar(){
     system("cls");
	system("color A");
//BORDES
gt(1,1);cout<< char(201);
gt(100,1);cout<< char(187);
gt(1,27);cout<< char(200);
gt(100,27);cout<< char(188);
	
//lineas verticales
for(int n=2;n<100;n++){
	gt(n,1);cout<< char(205);
	gt(n,7);cout<< char(205);
	gt(n,27);cout<< char(205);
     }
//LINEAS horizontales
for(int n=2;n<27;n++){
	gt(1,n); cout<< char(186);
	gt(100,n); cout<< char(186);
	 }
//CUADRILLAS
gt(1,7);cout<< char(204);
gt(100,7);cout<< char(185);
gt(30,3); cout<< "**Administrador De Contraseñas**";
//FECHA, HORAS
gt(3,5);cout<< __TIME__;
gt(80,5);cout<< __DATE__;  
}
int main(int argc, char** argv){
     NODO *cab=NULL;  
     string pag;
     string usuario;
     string password;
     int op,enter;
    	int contrasena;
	cout<<"--------------------------------\nProcess exited after 3.666 seconds with return value 0\nPresione una tecla para continuar . . .";
     HANDLE hconsole=GetStdHandle(STD_OUTPUT_HANDLE); 
	SetConsoleTextAttribute(hconsole,0);
	cin>>contrasena;
	if (contrasena==12465399) {
	do{
	system("cls");
     system("color a");
//ESQUINAS
gt(1,1);cout<< char(201);
gt(75,1);cout<< char(187);
gt(1,27);cout<< char(200);
gt(75,27);cout<< char(188);
//lineas verticales
for(int n=2;n<75;n++){
	gt(n,1);cout<< char(205);
	gt(n,7);cout<< char(205);
	gt(n,27);cout<< char(205);
     gt(n,23);cout<< char(205);}
//LINEAS horizontales
for(int n=2;n<27;n++){
	gt(1,n); cout<< char(186);
	gt(75,n); cout<< char(186);
 }
//DIVICIONES
gt(1,7);cout<< char(204);
gt(75,7);cout<< char(185);
gt(1,23);cout<< char(204);
gt(75,23);cout<< char(185);
gt(20,3); cout<< "**Administrador De Contraseñas**";
//FECHA, HORA                                                                                                                                           
gt(60,5);cout<< __DATE__;
gt(3,5);cout<< __TIME__;
		gt(2,8);cout<<"Menu:"<<endl;
		gt(2,10);cout<<" 1: Ingresar Nuevo Dato"<<endl;
		gt(2,11);cout<<" 2: Mostrar Datos"<<endl;
		gt(2,12);cout<<" 3: Guardar Datos"<<endl;
		gt(2,13);cout<<" 4: Cargar Datos"<<endl;
		gt(2,14);cout<<" 5: Generar Contraseña Numerica"<<endl;
		gt(37,10);cout<<" 6: Generar Contraseña Alfabetica"<<endl;
		gt(37,11);cout<<" 7: Generar Contraseña Alfanumerica"<<endl;
		gt(37,12);cout<<" 8: Generar Contraseña Cad. Car."<<endl;
		gt(37,13);cout<<" 9: Eliminar Archivo"<<endl;
		gt(37,14);cout<<" 0: Salir"<<endl;
		gt(2,24);cout<<"Mensaje: "<<endl;
		gt(2,16);cout<<"Su opción: ",cin>>op;
          switch(op){
               case 1://ingresa nueva contraseña
			     gt(2,18);cout<<"->Ingrese La Pagina: ";
			     cin>>pag;
                    gt(2,20);cout<<"->Ingrese El Usuario: ";
                    cin>>usuario;
                    gt(2,22);cout<<"->Ingrese Contraseña: ";
                    cin>>password;
                    registrarpassword(cab, pag, usuario, password);
                    cout<<"\n";
				gt(11,24);cout<<"Password Save...";
                    gt(2,26);break;
               case 2://muestra las contraseñas
                    ventanamostrar();
			     gt(2,8);cout<<"Lista:\n\n";mostrarNotas(cab);
				gt(30,25);break;
               case 3://guarda las contraseñas en un archivo "Datos_Estudiantes"
			     grabar(cab,"C:\\Users\\LATINA\\Desktop\\Ingenieria De Sistemas\\Datos_Estudiantes.txt");
			     grabar(cab,"C:\\Users\\LATINA\\Desktop\\Ingenieria De Sistemas\\salvaconducto");
                    gt(11,24);cout<<"Datos Guardados"<<endl;
				gt(2,26);break;
               case 4://exporta los archivos (contraseñas)
               	gt(11,24);
			     if((cab=cargar("C:\\Users\\LATINA\\Desktop\\Ingenieria De Sistemas\\Datos_Estudiantes.txt"))!=NULL)
                         cout<<"Datos Cargados"<<endl;
                         else
                         cout<<"Archivo De Datos Vacia"<<endl;    
                    gt(2,26);break;
               case 5://generar contraseña numerica
			     GenerarContrasenaNumerica();
				gt(2,26);break;     
			case 6://generar contraseña Alfabetica
                    generarContrasenaAlfabetica(24);
				gt(2,26);break;
			case 7://generar contraseña phonewords/Alfanumerica
			     generarContrasenaAlfaNumerica(24);
				gt(2,26);break;
			case 8://generar contraseña de cadena de caracteres
			     generarContrasenaCadenadeCaracteres(24)
				gt(2,26);break;
			case 9://elimina el archivo guardado
          		terminator();
          		gt(2,26);break;
			case 0:
			     gt(11,24);cout<<"Hasta Pronto..."<<endl;
				gt(2,26);break;
               default: gt(11,24);cout<<"Error En Opción";gt(2,26);
		}system("pause");
     }while(op!=0);return 0;}else{return 0;}}
