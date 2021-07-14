using System;

namespace HelloWord
{


    // criando classe
    class MinhaClasse
    {
        public void print(string str){
            Console.WriteLine(str);
        }

        //sobrecarga
        public void print(bool bl){
            Console.WriteLine(bl);
        }

        void printnum(int num){
            Console.WriteLine(num);
        }

        public void printbool(bool bl){
            Console.WriteLine(bl);
        }
    }



    // ligando classe
    class Outraclasse: MinhaClasse
    {
        //atributo
        public string coisa;
    }



    class Program
    {
        //definir tipos
        enum tipo {letra, numero, palavra}

        //pseudo classe p.1
        struct Pessoa{
            public string nome;
            public int idade;
        }


        static void Main(string[] args)
        {

            // coisas do terminal
            Console.ResetColor();
            Console.Beep();
            Console.Clear();
            Console.Title = "TESTANDO";



            int numero = 12;
            string nome = "jerson";
            double preco = 12.9;
            float jurus = 99.9f;
            char melhorLetra = 'ç';
            Console.WriteLine($"numero: {numero}, nome: {nome, 20}");
            Console.WriteLine("jurius {0:p}", jurus);
            Console.WriteLine("preço: {0:c}", preco);
            Console.WriteLine(melhorLetra);
            int[] nivers = new int[3]{12, 99, 32};
            char[] vogais = {'a', 'e', 'i', 'o', 'u'};



            // inputs
            ConsoleKeyInfo tecla = Console.ReadKey();
            Console.WriteLine(tecla.Key);
            int letra_para_hexa = Console.Read();


            //conversor universal
            byte saida = Convert.ToByte("iai");



            //condicionais
            Console.Write("nao mande cafe");
            string entrada = Console.ReadLine();
            if (entrada == "cafe"){
                Console.WriteLine("cafe é baaaaaauuuum");
            }
            else {
                Console.WriteLine($"tu escreveu {entrada} ?");
            }



            // declaraçao de listas
            string[] lista = {"cafe", "feijao", "arroz", "sapato"};
            Console.WriteLine("lista de compras");
            foreach (string coisa in lista) {
                Console.WriteLine(coisa);
            }



            // loops
            Console.WriteLine("ano NOVO!!!!");
            for (int c = 1; c <= 10; c++) {
                Console.WriteLine(c);
            }

            int ponto = 0;
            while (ponto == 0) {
                if (ponto != 0) {
                    Console.WriteLine("voce nao mandou 0!");
                    break;
                }
                else {
                    Console.Write("manda um numero ai: ");
                    ponto = int.Parse(Console.ReadLine());
                }
            }

            string produto = "cafe";
            do {
                Console.WriteLine("cafe");
                Console.Write(": ");
                produto = Console.ReadLine();
            } while (produto == "cafe");



            // switch
            switch (nome){
                case "eduardo":
                    Console.WriteLine("eduuuaaaaardoooooo");
                    break;
                case "josafa":
                    Console.WriteLine("josafaaaa");
                    break;
                default:
                    Console.WriteLine("nao gosto desse nome");
                    break;
            }


            //operador ternario
            //                   true : false
            preco = numero > 15 ? 22.2 : 0;



            // metodos de lista
            Console.WriteLine(vogais);
            Array.Reverse(vogais);
            Console.WriteLine(vogais);
            int posicao = Array.IndexOf(nivers, 99); // find()
            int posicao2 = Array.BinarySearch(nivers, 99); // verifica se o item existe
            Array.Sort(nivers);
            vogais.SetValue(0, 'f');


            //pseudo classe p.2
            Pessoa p1 = new Pessoa();
            p1.nome = "robson";

            Pessoa p2 = new Pessoa() {idade = 32, nome = "claudio"};


            //tipos
            tipo algo = tipo.letra;
            Console.WriteLine(algo);
            int index_tipo = (int)tipo.numero;
            Console.WriteLine(index_tipo);



            // criando classes
            MinhaClasse classe = new MinhaClasse();
            classe.printbool(true);

            Outraclasse classe2 = new Outraclasse();
            classe2.coisa = "cafe";
            classe2.printbool(false);

            Outraclasse classe3 = new Outraclasse() {coisa = "jerson"};
        }
    }
}
