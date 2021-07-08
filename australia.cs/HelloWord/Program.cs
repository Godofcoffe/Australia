using System;

namespace HelloWord
{
    class Program
    {
        static void Main(string[] args)
        {
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


            // metodos de lista
            Console.WriteLine(vogais);
            Array.Reverse(vogais);
            Console.WriteLine(vogais);
            int posicao = Array.IndexOf(nivers, 99); // find()
            int posicao2 = Array.BinarySearch(nivers, 99); // verifica se o item existe
            Array.Sort(nivers);
            vogais.SetValue(0, 'f');
        }
    }
}
