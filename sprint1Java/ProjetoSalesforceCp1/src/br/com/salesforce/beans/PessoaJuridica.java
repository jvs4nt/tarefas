package br.com.salesforce.beans;

public class PessoaJuridica extends Cadastro {

	
	
	private String cnpj;

	public PessoaJuridica() {
		super();
	}

	public PessoaJuridica(String primeiroNome, String sobreNome, String email, String senha, String cnpj) {
		super(primeiroNome, sobreNome, email, senha);
		this.cnpj = cnpj;
	}

	public String getCnpj() {
		return cnpj;
	}

	public void setCnpj(String cnpj) {
		this.cnpj = cnpj;
	}
	
	
	
}
