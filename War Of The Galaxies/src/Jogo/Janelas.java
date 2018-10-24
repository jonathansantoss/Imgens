package Jogo;

import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JSeparator;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Janelas extends JFrame {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	public Janelas() {

		JMenuBar barraMenu = new JMenuBar(); // Criar os Menus do Jogo
		JMenu menu = new JMenu("Menu");
		JMenuItem sobre = new JMenuItem("Sobre");
		sobre.addActionListener(new ActionListener() {

			public void actionPerformed(ActionEvent arg0) {

				JOptionPane.showMessageDialog(null,
						"Projeto Integrado - Engenharia da Computação - Desenvolvido Pelos Alunos: Fabiano Albino, Helton Moura, Valdecir Munhan",
						"Informações", JOptionPane.INFORMATION_MESSAGE);
			}
		});

		JMenuItem sair = new JMenuItem("Sair"); // Criação do menu de saida do
												// jogo
		sair.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});

		menu.add(sobre);
		menu.add(new JSeparator());
		menu.add(sair);

		barraMenu.add(menu); // Adicionando o menu na barra de menu
		setJMenuBar(barraMenu);

		add(new Fase());
		setTitle("War Of The Galaxies"); // Apresentar o titulo do jogo
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Fechar as janelas do
														// jogo
		setSize(1200, 630);// Resolução do jogo. Tamanho da janela.
		setLocationRelativeTo(null); // Janela ficara no meio da tela por causa
										// do null
		setResizable(false); // Impossibilita o usuário de alterar a resolução
								// do jogo
		setVisible(true); // Visible for true, faz mostrar a janela
	}

	public void executa() { // metodo para
							// execultas(instanciar) as
							// janelas
		new Janelas(); // Criando uma nova janelas para execulsão do jogo

	}

}
