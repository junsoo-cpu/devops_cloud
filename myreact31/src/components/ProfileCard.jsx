import "./ProfileCard.css";

function ProfileCard({
  profileImage,
  name,
  role,
  facebook_url,
  email,
  changePageName,
}) {
  return (
    <body className="member1">
      <section>
        <nav className="menu">
          <a href="#">
            <i className="fas fa-bars"></i>
          </a>
          <a href="#">
            <i className="far fa-sticky-note"></i>
          </a>
        </nav>
        <article className="profile">
          <img src={profileImage} alt="프로필 이미지" />

          <h1>{name}</h1>
          <h2>{role}</h2>

          <a href="#" className="btnView">
            VIEW MORE
          </a>
        </article>

        <ul class="contact">
          <li>
            <i className="fab fa-facebook-f"></i>
            <span>{facebook_url}</span>
          </li>
          <li>
            <i className="fas fa-envelope"></i>
            <span>{email}</span>
          </li>
        </ul>

        <nav className="others">
          <a className="on" onClick={() => changePageName("member1")}></a>
          <a className="on" onClick={() => changePageName("member2")}></a>
          <a className="on" onClick={() => changePageName("member3")}></a>
          <a className="on" onClick={() => changePageName("member4")}></a>
        </nav>
      </section>
    </body>
  );
}

export default ProfileCard;
