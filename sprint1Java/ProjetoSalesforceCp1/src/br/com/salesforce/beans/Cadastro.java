package br.com.salesforce.beans;

public class Cadastro {

	
	
	protected String primeiroNome;
	protected String sobreNome;
	protected String email;
	protected String senha;
	

	public Cadastro() {
		super();
	}
	
	public Cadastro(String primeiroNome, String sobreNome, String email, String senha) {
		super();
		this.primeiroNome = primeiroNome;
		this.sobreNome = sobreNome;
		this.email = email;
		this.senha = senha;
	}

	public String getPrimeiroNome() {
		return primeiroNome;
	}

	public void setPrimeiroNome(String primeiroNome) {
		this.primeiroNome = primeiroNome;
	}

	public String getSobreNome() {
		return sobreNome;
	}

	public void setSobreNome(String sobreNome) {
		this.sobreNome = sobreNome;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getSenha() {
		return senha;
	}

	public void setSenha(String senha) {
		this.senha = senha;
	}
	
	
	
}
