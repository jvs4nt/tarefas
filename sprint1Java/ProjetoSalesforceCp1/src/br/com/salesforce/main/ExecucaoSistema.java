package br.com.salesforce.main;

import javax.swing.JOptionPane;

import br.com.salesforce.beans.CampanhaMarketing;
import br.com.salesforce.beans.Cliente;
import br.com.salesforce.beans.Contato;
import br.com.salesforce.beans.Endereco;
import br.com.salesforce.beans.Produto;

public class ExecucaoSistema {

	public static void main(String[] args) {
		
		//(String nome, String empresa, String dtCadastro)
		Cliente objCliente = new Cliente(
				JOptionPane.showInputDialog("Digite o nome"),
				JOptionPane.showInputDialog("Digite o nome da empresa"),
				JOptionPane.showInputDialog("Digite a data do cadastro em formto dd/mm/yyyy")
				);
		
		//(String logradouro, int numero, String cep, String bairro, String cidade)
		Endereco objEndereco = new Endereco (
				JOptionPane.showInputDialog("Digite o logradouro"),
				Integer.parseInt(JOptionPane.showInputDialog("Digite o número")),
				JOptionPane.showInputDialog("Digite o cep"),
				JOptionPane.showInputDialog("Digite o bairro"),
				JOptionPane.showInputDialog("Digite a cidade")
				);
		objCliente.setEndereco(objEndereco);
		
		//(String nomeContato, String email, String numeroTelefone, String instagram)
		Contato objContato = new Contato (
				JOptionPane.showInputDialog("Digite o nome de  contato"),
				JOptionPane.showInputDialog("Digite o email"),
				JOptionPane.showInputDialog("Digite um número de telefone para contato"),
				JOptionPane.showInputDialog("Digite o instagram comercial")
				);
		objCliente.setContato(objContato);
		
		//(String nomeCampanha, String dataInicio, String dataFim, double orçamento,
		//String objetivoCampanha)
		CampanhaMarketing objCampanhaMarketing = new CampanhaMarketing(
				JOptionPane.showInputDialog("Digite o nome da Campanha"),
				JOptionPane.showInputDialog("Digite a data de inicio da campanha (dd/mm/yyyy)"),
				JOptionPane.showInputDialog("Digite a data de fim da campanha (dd/mm/yyyy)"),
				Double.parseDouble(JOptionPane.showInputDialog("Digite o valor do orçamento da campanha")),
				JOptionPane.showInputDialog("Digite o objetivo da campanha"));
		
		//(String nomeProduto, int idProduto, String descricao, double preco, String categoria)
		Produto objProduto = new Produto(
				JOptionPane.showInputDialog("Digite o nome do produto"),
				JOptionPane.showInputDialog("Digite a marca do produto"),
				Integer.parseInt(JOptionPane.showInputDialog("Digite o id do produto")),
				JOptionPane.showInputDialog("Digite a descrição do produto"),
				Double.parseDouble(JOptionPane.showInputDialog("Digite o preço do produto")),
				JOptionPane.showInputDialog("Digite a categoria do produto"));
		
		
		System.out.println("\nINFORMAÇÕES DO CLIENTE: " +
		"\nNome: " + objCliente.getNome()+
		"\nNome da empresa: " + objCliente.getEmpresa()+
		"\nData do cadastro: " + objCliente.getDtCadastro()+
		"\n\nINFORMAÇÕES DE ENDEREÇO: "	+
		"\nLogradouro: " + objCliente.getEndereco().getLogradouro()+
		"\nNúmero: " + objCliente.getEndereco().getNumero()+
		"\nCEP: " + objCliente.getEndereco().getCep()+
		"\nBairro: " + objCliente.getEndereco().getBairro()+
		"\nCidade: " + objCliente.getEndereco().getCidade()+
		"\n\nINFORMAÇÕES DE CONTATO: " +
		"\nNome de contato: " + objCliente.getContato().getNomeContato()+
		"\nEmail: " + objCliente.getContato().getEmail()+
		"\nNúmero para contato: " + objCliente.getContato().getNumeroTelefone()+
		"\nInstagram: " + objCliente.getContato().getInstagram()+
		"\n\nCAMPANHA DE MARKETING: " + 
		"\nNome da campanha: " + objCampanhaMarketing.getNomeCampanha()+
		"\nInicio da campanha: " + objCampanhaMarketing.getDataInicio()+
		"\nFim da campanha: " + objCampanhaMarketing.getDataFim()+
		"\nValor do orçamento: " + objCampanhaMarketing.getOrçamento()+
		"\nObjetivo da campanha: " + objCampanhaMarketing.getObjetivoCampanha()+
		"\n\nINFORMAÇÕES DO PRODUTO:" + 
		"\nNome: " + objProduto.getNomeProduto()+
		"\nMarca: " + objProduto.getMarca()+
		"\nId do produto: " + objProduto.getIdProduto()+
		"\nDescrição: " + objProduto.getDescricao()+
		"\nValor: " + objProduto.getPreco()+
		"\nCategoria: " + objProduto.getCategoria()
		);
		
	}

}
