package br.com.salesforce.main;

import javax.swing.JOptionPane;

import br.com.salesforce.beans.CampanhaMarketing;
import br.com.salesforce.beans.Cliente;
import br.com.salesforce.beans.Contato;
import br.com.salesforce.beans.Endereco;
import br.com.salesforce.beans.Produto;

public class ExecucaoSistema {

	//Métodos Static
	
		static String texto(String j) {
			return JOptionPane.showInputDialog(j);
		}
		
		static int inteiro(String j) {
			return Integer.parseInt(JOptionPane.showInputDialog(j));
		}
		
		static double real (String j) {
			return Double.parseDouble(JOptionPane.showInputDialog(j));
		}
	
	
	public static void main(String[] args) {
		
		//(String nome, String empresa, String dtCadastro)
		Cliente objCliente = new Cliente(
				texto("Digite o nome"),
				texto("Digite o nome da empresa"),
				texto("Digite a data do cadastro em formato dd/mm/yyyy")
				);
		
		//(String logradouro, int numero, String cep, String bairro, String cidade)
		Endereco objEndereco = new Endereco (
				texto("Digite o logradouro"),
				inteiro("Digite o número"),
				texto("Digite o cep"),
				texto("Digite o bairro"),
				texto("Digite a cidade")
				);
		objCliente.setEndereco(objEndereco);
		
		//(String nomeContato, String email, String numeroTelefone, String instagram)
		Contato objContato = new Contato (
				texto("Digite o nome de  contato"),
				texto("Digite o email"),
				texto("Digite um número de telefone para contato"),
				texto("Digite o instagram comercial")
				);
		objCliente.setContato(objContato);
		
		//(String nomeCampanha, String dataInicio, String dataFim, double orçamento,
		//String objetivoCampanha)
		CampanhaMarketing objCampanhaMarketing = new CampanhaMarketing(
				texto("Digite o nome da Campanha"),
				texto("Digite a data de inicio da campanha (dd/mm/yyyy)"),
				texto("Digite a data de fim da campanha (dd/mm/yyyy)"),
				real("Digite o valor do orçamento da campanha"),
				texto("Digite o objetivo da campanha"));
		
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
