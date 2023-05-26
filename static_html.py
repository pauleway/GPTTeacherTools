nav = """
<div class="container-fluid p-5 bg-primary text-white text-center">
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid text-white">
            <a class="navbar-brand" href="/">AI Teacher Tools</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup"
                    aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
             <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="#">Planning</a>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Communication
          </a>
          <ul class="dropdown-menu bg-primary">
            <li><a class="dropdown-item" href="/communication/student-email">Student Email Generator</a></li>
            <li><a class="dropdown-item" href="/communication/parent-email">Parent Email Generator</a></li>
            <li><a class="dropdown-item" href="#">*Course Narrative Generator</a></li>
            <li><a class="dropdown-item" href="/communication/student-narratives">Student Progress Narrative</a></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Assessment
          </a>
          <ul class="dropdown-menu bg-primary">
            <li><a class="dropdown-item" href="/assessment/formative-assessment">Formative Assessments</a></li>
            <li><a class="dropdown-item" href="/assessment/vocabulary-quiz">Vocab Quiz Generator</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
      </ul>
    </div>
        </div>
    </nav>
</div>

"""

scripts = """
<script src="/static/scripts.js"></script>
<link href="/static/styles.css" rel="stylesheet">
"""