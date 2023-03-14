using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace Base
{
    public partial class Form2 : Form
    {
        private bool b1;
        private bool b2;
        private bool b3;

        private bool z1;
        private bool z2;
        private bool z3;

        private string s1;
        private string s2;
        private string s3;

        private bool otpr;

        private int sec;
        private int ch;
        private int m;
        private int s;

        public Form2()
        {
            InitializeComponent();
            b1 = true;
            b2 = false;
            b3 = false;

            z1 = false;
            z2 = false;
            z3 = false;

            s1 = "";
            s2 = "";
            s3 = "";

            otpr = false;

            sec = 5_400;
            timer1.Start();

            textBox1.ForeColor = Color.DimGray;
            textBox1.Text = "введите ваше решение...";

            label1.Text = "Записан рост (в сантиметрах) пяти учащихся: \n158, 166, 134, 130, 132. На сколько отличается \nсреднее арифметическое этого набора чисел от его медианы?";
            label2.Text = "000";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            b1 = true;
            b2 = false;
            b3 = false;

            textBox1.Text = "";
            label1.Text = "Записан рост (в сантиметрах) пяти учащихся: \n158, 166, 134, 130, 132. На сколько отличается \nсреднее арифметическое этого набора чисел от его медианы?";
            
            if (!z1)
            {
                textBox1.ForeColor = Color.DimGray;
                textBox1.Text = "введите ваше решение...";
            }
            else
            {
                textBox1.ForeColor = Color.Black;
                textBox1.Text = s1;
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            b1 = false;
            b2 = true;
            b3 = false;

            label1.Text =
            textBox1.Text = "Высота равностороннего треугольника равна 15 корень из 3.\nНайдите его периметр.";

            if (!z2)
            {
                textBox1.ForeColor = Color.DimGray;
                textBox1.Text = "введите ваше решение...";
            }
            else
            {
                textBox1.ForeColor = Color.Black;
                textBox1.Text = s2;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            b1 = false;
            b2 = false;
            b3 = true;

            label1.Text = "Периметр ромба равен 40, а один из углов равен 30°.\nНайдите площадь ромба.";
            textBox1.Text = "";

            if (!z3)
            {
                textBox1.ForeColor = Color.DimGray;
                textBox1.Text = "введите ваше решение...";
            }
            else
            {
                textBox1.ForeColor = Color.Black;
                textBox1.Text = s3;
            }
        }

        private void textBox1_Click(object sender, EventArgs e)
        {
            textBox1.ForeColor = Color.Black;
            textBox1.Text = "";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "" || textBox1.Text != "введите ваше решение...")
            {
                if (b1)
                {
                    s1 = textBox1.Text;
                    z1 = true;
                }
                else if (b2)
                {
                    s2 = textBox1.Text;
                    z2 = true;
                }
                else if (b3)
                {
                    s3 = textBox1.Text;
                    z3 = true;
                }
            }
            else if (textBox1.Text == "" || textBox1.Text == "введите ваше решение...")
            {
                textBox1.ForeColor = Color.Red;
                textBox1.Text = "тут нет ответа";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (s >= 1)
            {
                if (MessageBox.Show("Вы точно хотите завершить?", "Question", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
                {
                    otpr = true;
                }
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            sec--;
            ch = sec / 3600;
            m = (sec - ch * 3600) / 60;
            s = (sec - ch * 3600) - m * 60;

            label2.Text = $"{ch}Ч {m}М {s}С";

            if (s == 0)
            {
                otpr = true;
                timer1.Stop();
            }

            if (otpr == true)
            {
                timer1.Stop();
                //тут будет отправка на сервер
                MessageBox.Show("тест закончен, понравилась ли вам система сдачи экзамена?", "Question", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                //File.WriteAllText("C:\\Users\\svatoslav\\Downloads\\EXEZE\\GUI\\python\\v.txt", "true");
                File.WriteAllText("v.txt", "true");
                Application.Exit();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (s >= 1)
            {
                if (MessageBox.Show("Вы точно хотите завершить?", "Question", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
                {
                    otpr = true;
                }
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("У вас 60 секунд", "fact", MessageBoxButtons.OK, MessageBoxIcon.Question) == DialogResult.OK)
            {
                //File.WriteAllText("C:\\Users\\svatoslav\\Downloads\\EXEZE\\GUI\\python\\tul.txt", "true");
                File.WriteAllText("tul.txt", "true");
            }
        }
    }
}
