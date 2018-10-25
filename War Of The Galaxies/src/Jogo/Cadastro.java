package Jogo;

import java.awt.Color;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.JButton;
import javax.swing.JPanel;

@SuppressWarnings("serial")
public class Cadastro extends JPanel implements MouseListener {
	private JButton btnNovoJogo;
	private boolean cadastroFase;

	public Cadastro() {
		
		
		btnNovoJogo = new JButton("Novo Jogo");
		btnNovoJogo.setBounds(10, 10, 100, 100);
		
		cadastroFase = false;

		btnNovoJogo.addMouseListener(this);
		
		setBackground(Color.BLACK);
		
		GridBagConstraints regras= new GridBagConstraints();
		GridBagLayout grid = new GridBagLayout();
		setLayout(grid);
		
		regras.fill = GridBagConstraints.NONE;
		regras.anchor = GridBagConstraints.CENTER;
		regras.weightx = 10;
		regras.weighty = 10;
		regras.gridx = 1;
		regras.gridy = 1;
		regras.gridwidth = 10;
		regras.gridheight = 10;
		
		grid.setConstraints(btnNovoJogo, regras);
		add(btnNovoJogo);
	}

	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		if (e.getSource() == btnNovoJogo) {
			cadastroFase = true;
		}
	}

	@Override
	public void mouseEntered(MouseEvent arg0) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseExited(MouseEvent arg0) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mousePressed(MouseEvent arg0) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseReleased(MouseEvent arg0) {
		// TODO Auto-generated method stub

	}

	public boolean isCadastroFase() {
		return cadastroFase;
	}

}
