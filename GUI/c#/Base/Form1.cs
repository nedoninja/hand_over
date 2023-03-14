using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Threading;

namespace Base
{
    public partial class Form1 : Form
    {
        private Thread thread;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            startInfo.FileName = "cmd.exe";
            //startInfo.Arguments = "/C python C:\\Users\\svatoslav\\Downloads\\EXEZE\\GUI\\python\\comp.py";
            startInfo.Arguments = "/C comp.exe";
            process.StartInfo = startInfo;
            process.Start();
            Close();
            thread = new Thread(openForm2);
            thread.SetApartmentState(ApartmentState.STA);
            thread.Start();
        }

        private void openForm2(object obj)
        {
            Application.Run(new Form2());
        }
    }
}
