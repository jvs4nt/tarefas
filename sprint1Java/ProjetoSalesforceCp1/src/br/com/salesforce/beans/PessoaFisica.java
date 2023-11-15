package br.com.salesforce.beans;

public class PessoaFisica extends Cadastro {

	
	private String cpf;

	public PessoaFisica() {
		super();
	}

	public PessoaFisica(String primeiroNome, String sobreNome, String email, String senha, String cpf) {
		super(primeiroNome, sobreNome, email, senha);
		this.cpf = cpf;
	}

	public String getCpf() {
		return cpf;
	}

	public void setCpf(String cpf) {
		this.cpf = cpf;
	}
	
	
	
	
	
}
